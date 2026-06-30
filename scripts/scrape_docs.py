#!/usr/bin/env python3
"""Scrape UnifyApps conceptual docs (everything except unify-integrations connectors)
into clean local markdown, with images downloaded locally. Local-first knowledge base.

Re-runnable. Flags:
  --force      re-process & overwrite existing .md files
  --no-images  skip downloading images (text only)
Handles: h2-h6, paragraphs, nested ul/ol lists, inline code, bold/italic, links,
note-wrapper callouts, tables, code blocks, and images (downloaded to <section>/_img/)."""
import os, re, sys, html, time, hashlib, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
URLS_FILE = "/tmp/ua_docs_urls.txt"
SITEMAP = "https://www.unifyapps.com/sitemap.xml"
BASE = "https://www.unifyapps.com"

FORCE = "--force" in sys.argv
NO_IMAGES = "--no-images" in sys.argv

SECTION_MAP = {
    "unify-applications": "applications", "unify-automations": "automations",
    "unify-data": "data", "unify-agentic-ai": "agentic-ai",
    "platform-tools": "platform-tools", "governance": "governance",
    "embedded-integrations": "embedded-integrations",
}
SKIP_SECTION = "unify-integrations"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

_img_cache = {}          # real_url -> local filename (dedup across pages)
import threading
_img_lock = threading.Lock()


def http_get(url, binary=False, tries=3, headers=None):
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "ignore")
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(1.5 * (i + 1))
    return None


def real_img_url(src):
    if not src:
        return None
    if src.startswith("/_next/image"):                    # next image proxy -> unwrap ?url=
        q = urllib.parse.urlparse(src).query
        u = urllib.parse.parse_qs(q).get("url", [None])[0]
        if u:
            src = u
    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        src = BASE + src
    return src


IMG_WIDTH = 1920   # allowed Next deviceSize; optimizer -> small WebP, not full-res CDN original

def save_image(src, imgdir):
    if NO_IMAGES:
        return None
    url = real_img_url(src)
    if not url or not url.startswith("http"):
        return None
    with _img_lock:
        if url in _img_cache:
            return _img_cache[url]
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower()
    if ext == ".svg":                                  # vector: fetch as-is (tiny)
        fetch_url, save_ext = url, ".svg"
    else:                                              # raster: optimize -> WebP, capped width
        fetch_url = f"{BASE}/_next/image?url={urllib.parse.quote(url, safe='')}&w={IMG_WIDTH}&q=72"
        save_ext = ".webp"
    name = hashlib.md5(url.encode()).hexdigest()[:16] + save_ext
    os.makedirs(imgdir, exist_ok=True)
    out = os.path.join(imgdir, name)
    if not os.path.exists(out):
        accept = {"Accept": "image/webp,image/avif,image/*,*/*"}
        data = http_get(fetch_url, binary=True, headers=accept)
        if not data:
            return None
        with open(out, "wb") as f:
            f.write(data)
    with _img_lock:
        _img_cache[url] = name
    return name


class Conv:
    """HTML(article) -> Markdown, with images saved under imgdir (referenced as _img/<name>)."""
    def __init__(self, imgdir):
        self.imgdir = imgdir

    def img_md(self, el):
        src = el.get("src") or el.get("data-src")
        name = save_image(src, self.imgdir)
        alt = (el.get("alt") or "").strip()
        if name:
            return f"![{alt}](_img/{name})"
        return f"![{alt}]({real_img_url(src) or ''})" if src else ""

    def _note_text(self, c):
        body = c.find(class_=lambda x: x and "content-wrapper" in x)  # note body, sans icon+label
        t = self.inline(body if body else c)
        t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)            # drop the note icon image
        t = re.sub(r"\s+", " ", t).strip()
        t = re.sub(r"^Note\s*[:.]?\s*", "", t)                 # strip any stray "Note" label
        t = re.sub(r"^Note(?=[A-Z])", "", t)
        return t.strip()

    def _wrap(self, c, left, right, plain=False):
        # wrap inline content in markers, preserving surrounding whitespace
        raw = c.get_text() if plain else self.inline(c)
        t = raw.strip()
        if not t:
            return " " if raw else ""           # whitespace-only tag -> a space (don't glue words)
        lead = " " if raw[:1].isspace() else ""
        trail = " " if raw[-1:].isspace() else ""
        return f"{lead}{left}{t}{right}{trail}"

    def inline(self, el):
        parts = []
        for c in el.children:
            if isinstance(c, NavigableString):
                parts.append(str(c))
            elif isinstance(c, Tag):
                n = c.name
                cls = " ".join(c.get("class", []))
                if n in ("ul", "ol"):
                    continue                       # block lists handled separately
                elif "note-wrapper" in cls or "callout" in cls:
                    parts.append(" **Note:** " + self._note_text(c) + " ")
                elif n in ("strong", "b"):
                    parts.append(self._wrap(c, "**", "**"))
                elif n in ("em", "i"):
                    parts.append(self._wrap(c, "*", "*"))
                elif n == "code":
                    parts.append(self._wrap(c, "`", "`", plain=True))  # plain: no nested **
                elif n == "a":
                    parts.append(f"[{self.inline(c).strip()}]({c.get('href','')})")
                elif n == "img":
                    parts.append("\n\n" + self.img_md(c) + "\n\n")     # image on its own line
                elif n == "br":
                    parts.append(" ")
                else:
                    parts.append(self.inline(c))
        return re.sub(r"[ \t]+", " ", "".join(parts))

    def render_list(self, el, depth):
        # items: <li>s whose nearest list ancestor is THIS list (survives wrapper divs/p)
        items = [li for li in el.find_all("li") if li.find_parent(["ul", "ol"]) is el]
        lines, ordered, i = [], el.name == "ol", 1
        for li in items:
            marker = f"{i}. " if ordered else "- "
            indent = "  " * depth
            raw = self.inline(li)
            imgs = re.findall(r"!\[[^\]]*\]\([^)]*\)", raw)        # pull images out of the bullet
            text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", raw)
            text = re.sub(r"\s+", " ", text).strip()
            lines.append(f"{indent}{marker}{text}" if text else f"{indent}{marker}".rstrip())
            for im in imgs:                                         # images on their own indented line
                lines.append(f"{indent}  {im}")
            # nested lists: those whose nearest <li> ancestor is THIS li (may sit inside a <p>/div)
            for sub in [l for l in li.find_all(["ul", "ol"]) if l.find_parent("li") is li]:
                lines.extend(self.render_list(sub, depth + 1))
            i += 1
        return lines

    def render_table(self, el):
        rows = []
        for tr in el.find_all("tr"):
            cells = [self.inline(td).strip() for td in tr.find_all(["td", "th"])]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        w = max(len(r) for r in rows)
        rows = [r + [""] * (w - len(r)) for r in rows]
        out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * w]
        for r in rows[1:]:
            out.append("| " + " | ".join(r) + " |")
        return "\n".join(out)

    def walk(self, el):
        out = []
        for c in el.children:
            if isinstance(c, NavigableString):
                t = str(c).strip()
                if t:
                    out.append(t)
                continue
            if not isinstance(c, Tag):
                continue
            n = c.name
            cls = " ".join(c.get("class", []))
            if "note-wrapper" in cls or "callout" in cls:
                t = self._note_text(c)
                if t:
                    out.append("> **Note:** " + t.replace("\n", " "))
            elif n in ("h1", "h2", "h3", "h4", "h5", "h6"):
                out.append("#" * int(n[1]) + " " + self.inline(c).strip())
            elif n == "p":
                t = self.inline(c).strip()
                if t:
                    out.append(t)
            elif n in ("ul", "ol"):
                out += self.render_list(c, 0)
            elif n == "table":
                t = self.render_table(c)
                if t:
                    out.append(t)
            elif n == "pre":
                out.append("```\n" + c.get_text().strip() + "\n```")
            elif n == "img":
                m = self.img_md(c)
                if m:
                    out.append(m)
            elif n in ("script", "style", "nav", "button"):
                continue
            else:
                out += self.walk(c)                # recurse into wrapper containers
        return out


def to_markdown(raw_html, imgdir):
    soup = BeautifulSoup(raw_html, "html.parser")
    art = soup.find("article")
    if not art:
        return None
    lines = Conv(imgdir).walk(art)
    md = "\n\n".join(x for x in lines if x.strip())
    md = re.sub(r"\n{3,}", "\n\n", md)
    # collapse runs of the same image (responsive dup <img> tags share one local path)
    md = re.sub(r"(!\[[^\]]*\]\((_img/[^)]+)\))(?:\s*!\[[^\]]*\]\(\2\))+", r"\1", md)
    # keep nested list blocks tight (no blank line between consecutive list items)
    md = re.sub(r"(^[ \t]*(?:- |\d+\. ).*)\n\n(?=[ \t]*(?:- |\d+\. ))", r"\1\n", md, flags=re.M)
    return md.strip()


def title_of(raw_html, slug):
    m = re.search(r"<title[^>]*>(.*?)</title>", raw_html, flags=re.S)
    if m:
        t = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
        t = re.sub(r"\s*[-|]\s*UnifyApps.*$", "", t)
        if t:
            return t
    return slug.replace("-", " ").title()


def parse(url):
    rest = url.split("/docs/", 1)[1] if "/docs/" in url else ""
    parts = [p for p in rest.split("/") if p]
    if not parts:
        return None
    section = parts[0]
    if section == SKIP_SECTION or section not in SECTION_MAP:
        return None
    slug = "-".join(parts[1:]) if len(parts) > 1 else "overview"
    return SECTION_MAP[section], slug


def work(url):
    p = parse(url)
    if not p:
        return ("skip", url)
    folder, slug = p
    outdir = os.path.join(DOCS, folder)
    imgdir = os.path.join(outdir, "_img")
    out = os.path.join(outdir, slug + ".md")
    if os.path.exists(out) and os.path.getsize(out) > 200 and not FORCE:
        return ("exists", url)
    raw = http_get(url)
    if not raw:
        return ("fetch-fail", url)
    md = to_markdown(raw, imgdir)
    if not md or len(md) < 60:
        return ("no-content", url)
    title = title_of(raw, slug)
    os.makedirs(outdir, exist_ok=True)
    with open(out, "w") as f:
        f.write(f"# {title}\n\nSource: {url}\nSection: {folder}\n\n---\n\n{md}\n")
    return ("saved", url)


def ensure_urls():
    if os.path.exists(URLS_FILE) and os.path.getsize(URLS_FILE) > 100:
        return
    xml = http_get(SITEMAP) or ""
    urls = re.findall(r"https://www\.unifyapps\.com/docs[^<\s]*", xml)
    with open(URLS_FILE, "w") as f:
        f.write("\n".join(sorted(set(urls))))


def main():
    ensure_urls()
    with open(URLS_FILE) as f:
        urls = sorted({l.strip() for l in f if l.strip() and "/docs/" in l})
    todo = [u for u in urls if parse(u)]
    print(f"{len(urls)} docs URLs; {len(todo)} conceptual to process "
          f"(force={FORCE}, images={'off' if NO_IMAGES else 'on'})")
    counts = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(work, u): u for u in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            status, url = fut.result()
            counts[status] = counts.get(status, 0) + 1
            if status in ("fetch-fail", "no-content"):
                print(f"  [{status}] {url}")
            if i % 40 == 0:
                print(f"  ...{i}/{len(todo)}  {dict(counts)}")
    print("DONE:", counts, "| images saved:", len(_img_cache))


if __name__ == "__main__":
    main()
