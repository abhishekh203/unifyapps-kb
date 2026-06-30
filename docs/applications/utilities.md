# Utilities

Source: https://www.unifyapps.com/docs/unify-applications/utilities
Section: applications

---

## **Date & Time**

### **formatDate**

Format a date value using a custom format pattern.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| date | Date | string | number | Yes | Date object, epoch timestamp (ms), or stringified number |
| formatStr | string | Yes | Format pattern (date-fns tokens) |

**Returns:** Formatted date string, empty string if invalid

**Examples**

`// basic formatting
{{ utils.formatDate(new Date(), 'dd-MM-yyyy') }}
// → 26-10-2025

// with time
{{ utils.formatDate(new Date(), 'dd-MM-yyyy HH:mm:ss') }}
// → 26-10-2025 14:30:45

// epoch timestamp
{{ utils.formatDate(1729944645000, 'MMM dd, yyyy') }}
// → Oct 26, 2025

// from data source
{{ utils.formatDate({{ userRecord.createdTime }}, 'dd-MMM-yyyy') }}
// → 26-Oct-2025`

**Common Patterns**

| Pattern | Output |
|---|---|
| dd-MM-yyyy | 26-10-2025 |
| MM/dd/yyyy | 10/26/2025 |
| yyyy-MM-dd | 2025-10-26 |
| MMM dd, yyyy | Oct 26, 2025 |
| dd/MM/yyyy HH:mm | 26/10/2025 14:30 |
| h:mm a | 2:30 PM |

[Full list of date-fns tokens](https://date-fns.org/docs/format)

### **formatDateByFormatType**

Format dates using predefined format types. Includes relative time formatting ("2 hours ago").

**Parameters**

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| date | Date | string | number | Yes | - | Date object, epoch timestamp (ms), or stringified number |
| formatType | string | No | 'mdyhm' | Predefined format type or custom pattern |
| options | FormatDistanceOptions | No | - | Options forrelative-time-to-nowonly |

**Format Types**

| Type | Output Example |
|---|---|
| mdyhm(default) | 10/26/2025 14:30 |
| dmyhms | 26 Oct 2025, 14:30:45 |
| yyyyMMdd | 2025-10-26 |
| iso | 2025-10-26T14:30:45+00:00 |
| relative-time-to-now | 2 hours ago |

[See all format types](https://markdownlivepreview.com/#format-type-reference)

**Examples**

`// default format
{{ utils.formatDateByFormatType(new Date()) }}
// → 10/26/2025 14:30

// specific format
{{ utils.formatDateByFormatType(new Date(), 'dmyhms') }}
// → 26 Oct 2025, 14:30:45

// relative time
{{ utils.formatDateByFormatType({{ lastLogin }}, 'relative-time-to-now') }}
// → 2 hours ago

// with options (relative time only)
{{ utils.formatDateByFormatType({{ lastLogin }}, 'relative-time-to-now', { includeSeconds: true }) }}
// → 2 hours 15 minutes 30 seconds ago`

### **formatTime**

Convert milliseconds into a human-readable duration (e.g., "1h 30m 15s" ).

**Parameters**

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| ms | number | Yes | - | Duration in milliseconds |
| precision | 'years' | 'months' | 'days' | 'hours' | 'minutes' | 'seconds' | 'milliseconds' | No | 'milliseconds' | Lowest time unit to display |
| notation | 'comfortable' | 'compact' | No | 'compact' | 'compact': "1h 30m",'comfortable': "1 hour 30 minutes" |
| maxSignificantUnits | number | No | 7 | Max number of units to show |

**Examples**

`// basic duration
{{ utils.formatTime(5415000) }}
// → 1h 30m 15s

// limit precision
{{ utils.formatTime(3661005, 'minutes') }}
// → 1h 1m

// comfortable notation
{{ utils.formatTime(5415000, 'seconds', 'comfortable') }}
// → 1 hour 30 minutes 15 seconds

// limit units shown
{{ utils.formatTime(269329401003, 'milliseconds', 'compact', 2) }}
// → 8y 6mo

// uptime display
System uptime: {{ utils.formatTime({{ uptimeMs }}, 'seconds') }}
// → System uptime: 15d 6h 32m 18s`

## **Numbers**

### **formatNumber**

Format numbers with locale support, compact notation (1.2K, 3.4M), and units.

**Parameters**

Single object parameter with these properties:

| Property | Type | Required | Description |
|---|---|---|---|
| value | number | Yes | Number to format |
| locale | string | No | Locale (e.g., 'en-US', 'de-DE') |
| maximumFractionDigits | number | No | Max decimal places |
| notation | 'standard' | 'scientific' | 'compact' | 'text' | No | Format style (default: 'standard') |
| compactDisplay | 'short' | 'long' | No | For compact: 'short' = "1.5K", 'long' = "1.5 thousand" |
| unit | string | No | Unit (e.g., 'percent', 'kilometer', 'byte') |
| unitDisplay | 'short' | 'long' | No | Unit display style |
| padDecimalPlaces | boolean | No | Pad decimals (5.5 → 5.50) |

**Examples**

`// basic formatting
{{ utils.formatNumber({ value: 1234.567, maximumFractionDigits: 2 }) }}
// → 1,234.57

// compact notation
{{ utils.formatNumber({ value: 1500000, notation: 'compact', compactDisplay: 'short' }) }}
// → 1.5M

// with units
{{ utils.formatNumber({ value: 0.856, unit: 'percent' }) }}
// → 85.6%

{{ utils.formatNumber({ value: 42.5, unit: 'kilometer' }) }}
// → 42.5 km

// locale-specific
{{ utils.formatNumber({ value: 1234.56, locale: 'de-DE' }) }}
// → 1.234,56

// dashboard metric
Total Users: {{ utils.formatNumber({ value: {{ totalUsers }}, notation: 'compact' }) }}
// → Total Users: 1.2M`

**Common Units**

| Category | Units |
|---|---|
| Length | meter kilometer mile |
| Mass | kilogram pound |
| Temperature | celsius fahrenheit |
| Digital | byte kilobyte megabyte gigabyte |
| Other | percent |

## **JSON**

### **parseJson**

Safely parse JSON strings. Never throws errors—returns fallback value on failure.

**Parameters**

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| str | string | Yes | - | JSON string to parse |
| fallback | T | No | {} | Value returned if parsing fails |
| retriever | function | No | - | Custom reviver function |

**Examples**

`// basic parsing
{{ utils.parseJson('{"name": "John", "age": 30}') }}
// → { name: "John", age: 30 }

// with fallback
{{ utils.parseJson('invalid json', { error: true }) }}
// → { error: true }

// parse API response
{{ utils.parseJson({{ apiResponse }}, { success: false, data: [] }) }}

// parse stored settings
{{ utils.parseJson({{ userSettings }}, { theme: 'light', lang: 'en' }).theme }}
// → 'light'`

### **stringifyJson**

Safely convert objects to JSON strings. Never throws errors—returns fallback on failure (e.g., circular references).

**Parameters**

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| obj | unknown | Yes | - | Object to stringify |
| fallback | T | No | null | Value returned if stringify fails |
| space | number | No | 0 | Spaces for indentation (pretty print) |
| replacer | function | No | - | Custom replacer function |

**Examples**

`// basic stringify
{{ utils.stringifyJson({ name: "John", age: 30 }) }}
// → '{"name":"John","age":30}'

// pretty print
{{ utils.stringifyJson({ name: "John", age: 30 }, null, 2) }}
// → '{
// "name": "John",
// "age": 30
// }'

// with fallback
{{ utils.stringifyJson({{ circularObject }}, '{}') }}
// → '{}'

// prepare for API
{{ utils.stringifyJson({ userId: {{ user.id }}, action: "update" }) }}

// filter sensitive data
{{ utils.stringifyJson(
 {{ userData }},
 null,
 0,
 (key, value) => key === 'password' ? undefined : value
) }}`

## **Reference**

### **Format Type Reference**

Complete list of formatDateByFormatType format types:

| Type | Pattern | Example |
|---|---|---|
| mdyhm | MM/dd/yyyy H:mm | 10/26/2025 14:30 |
| dmyhms | dd MMM yyyy, H:mm:ss | 26 Oct 2025, 14:30:45 |
| dmhms | dd MMM, H:mm:ss | 26 Oct, 14:30:45 |
| dmyhma | dd MMM yyyy, H:mm a | 26 Oct 2025, 2:30 PM |
| dmyhm | dd MMM yyyy, H:mm | 26 Oct 2025, 14:30 |
| mdyhma | MMM dd, yyyy h:mm a | Oct 26, 2025 2:30 PM |
| mdhma | MMM dd, h:mma | Oct 26, 2:30PM |
| Mdy | MMMM dd, yyyy | October 26, 2025 |
| dMy | d MMM yyyy | 26 Oct 2025 |
| yyyyMMdd | yyyy-MM-dd | 2025-10-26 |
| ddMMyyyy | dd-MM-yyyy | 26-10-2025 |
| ddMMyyyyhma | dd-MM-yyyy h:mm a | 26-10-2025 2:30 PM |
| ddMMM | dd MMM | 26 Oct |
| iso | yyyy-MM-dd'T'HH:mm:ssxxx | 2025-10-26T14:30:45+00:00 |
| hma | h:mm a | 2:30 PM |
| DayMMddyyyy | EEEE, MM-dd-yyyy | Sunday, 10-26-2025 |
| relative-time-to-now | - | 2 hours ago |

## **Resources**

- [date-fns format tokens](https://date-fns.org/docs/format)
- [Intl.NumberFormat API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)
