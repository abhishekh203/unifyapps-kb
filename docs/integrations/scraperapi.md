# ScraperAPI connector

Source: https://www.unifyapps.com/docs/unify-integrations/scraperapi
Section: integrations

---

ScraperAPI is a web scraping service that allows developers to extract data from websites without managing proxies, browsers, or CAPTCHAs. It handles IP rotation, retries, geolocation targeting, JavaScript rendering, and anti-bot bypassing automatically. ScraperAPI enables reliable data extraction for use cases such as price monitoring, market research, SEO tracking, and competitive intelligence.

## Authentication:

Integrating your application with ScraperAPI allows you to scrape web pages securely and at scale. Before starting, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. Example: "MyAppScraperAPIIntegration".
- `API Key`**:** Enter your ScraperAPI API key. This key authenticates all scraping requests.

## ACTIONS:

| **Action Name** | **Description** |
|---|---|
| `Scrape URL` | Fetches the HTML content of a specified URL using ScraperAPI with automatic proxy rotation and anti-bot handling. |
