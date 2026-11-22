# Trustpilot Reviews Scraper: Trustpilot Scraper API for Python & Node.js (2026)

Scrape Trustpilot reviews for any company: star rating, title, text, date, country, verification and company reply. No login needed. Export to JSON or CSV.

**[▶ Try the Trustpilot Reviews Scraper free on Scrapely](https://scrape.ly/store/cornerledger/trustpilot-scraper)** · [Compare Scrapely vs other scraping tools](https://scrape.ly/compare)

This repository shows how to scrape Trustpilot data with the [Trustpilot Reviews Scraper](https://scrape.ly/store/cornerledger/trustpilot-scraper) using the official
**Scrapely SDKs for JavaScript and Python**. You pass the input, Scrapely runs the trustpilot scraper in the cloud
(proxies, retries, browser and scaling included) and returns clean, structured data as JSON, CSV or Excel.
No scraper code to maintain and no blocked requests to debug.

## Why use this Trustpilot scraper

- **No-code or API:** run it from the [Scrapely Store](https://scrape.ly/store/cornerledger/trustpilot-scraper) or from your code with the SDK.
- **Structured trustpilot data:** ready-to-use fields instead of raw HTML.
- **Pay per result:** $0.49 per 1,000 review results, no monthly subscription required.
- **Maintained and monitored:** scrapers are tested around the clock and fixed fast when Trustpilot changes.
- **Integrations:** n8n, Make, Zapier, LangChain, LlamaIndex, MCP (Claude, Cursor) and webhooks.

## What Trustpilot data can you extract?

Scrape Trustpilot reviews for any company: star rating, title, text, date, country, verification and company reply. No login needed. Export to JSON or CSV.

| Output field |
|---|
| `rating` |
| `title` |
| `text` |
| `reviewerName` |
| `reviewerCountry` |
| `isVerified` |
| `publishedDate` |
| `language` |
| `businessName` |
| `url` |

## Quick start

1. [Sign up for Scrapely](https://scrape.ly) (free plan available) and copy your API token from
   **Settings → API & Integrations**.
2. Clone this repo and set your token:

```bash
export SCRAPELY_TOKEN=your_token
```

### Node.js (JavaScript SDK)

```bash
npm install
node example.js
```

```js
const { ScrapelyClient } = require('scrapely-client');
const client = new ScrapelyClient({ token: process.env.SCRAPELY_TOKEN });

const run = await client.actor('cornerledger/trustpilot-scraper').call({"startUrls": ["https://www.trustpilot.com/review/www.bankfive.com"], "maxReviews": 10, "sortBy": "recent", "sampling": "recent", "scrapeAllReviews": true, "filterDateRange": "all", "filterVerifiedOnly": false, "filterRepliesOnly": false, "strictNameMatch": false, "includeCompanyDetails": false, "includeStats": false, "proxyConfiguration": {"useScrapelyProxy": true, "scrapelyProxyGroups": ["DATACENTER"]}});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
```

### Python (Python SDK)

```bash
pip install -r requirements.txt
python example.py
```

```python
from scrapely_client import ScrapelyClient
client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

run = client.actor('cornerledger/trustpilot-scraper').call(run_input={ "startUrls": [ "https://www.trustpilot.com/review/www.bankfive.com" ], "maxReviews": 10, "sortBy": "recent", "sampling": "recent", "scrapeAllReviews": True, "filterDateRange": "all", "filterVerifiedOnly": False, "filterRepliesOnly": False, "strictNameMatch": False, "includeCompanyDetails": False, "includeStats": False, "proxyConfiguration": { "useScrapelyProxy": True, "scrapelyProxyGroups": [ "DATACENTER" ] } })
items = list(client.dataset(run.default_dataset_id).iterate_items())
```

### REST API / cURL

```bash
curl -X POST "https://api.scrape.ly/v2/acts/cornerledger~trustpilot-scraper/run-sync-get-dataset-items?token=$SCRAPELY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Example input

```json
{
  "startUrls": [
    "https://www.trustpilot.com/review/www.bankfive.com"
  ],
  "maxReviews": 10,
  "sortBy": "recent",
  "sampling": "recent",
  "scrapeAllReviews": true,
  "filterDateRange": "all",
  "filterVerifiedOnly": false,
  "filterRepliesOnly": false,
  "strictNameMatch": false,
  "includeCompanyDetails": false,
  "includeStats": false,
  "proxyConfiguration": {
    "useScrapelyProxy": true,
    "scrapelyProxyGroups": [
      "DATACENTER"
    ]
  }
}
```

See every input option on the [Trustpilot Reviews Scraper page](https://scrape.ly/store/cornerledger/trustpilot-scraper).

## Pricing

**$0.49 per 1,000 review results.** Free plan available, no credit card needed to start. Check current pricing on the
[Store page](https://scrape.ly/store/cornerledger/trustpilot-scraper) and see how Scrapely compares with other tools on [scrape.ly/compare](https://scrape.ly/compare).

## FAQ

**How do I scrape Trustpilot with Python?** Install `scrapely-client-python`, set `SCRAPELY_TOKEN` and run
`example.py`. The scraper runs on Scrapely and you read the results from the dataset.

**How do I scrape Trustpilot with Node.js?** Install `scrapely-client`, set `SCRAPELY_TOKEN` and run `example.js`.

**Is there a trustpilot scraper API?** Yes. Call `POST https://api.scrape.ly/v2/acts/cornerledger~trustpilot-scraper/runs`
or use `run-sync-get-dataset-items` to get results in one request.

**Do I need proxies?** No. Proxies, retries and browsers are handled by Scrapely.

**Is scraping Trustpilot legal?** This scraper collects publicly available data. Check Trustpilot's terms and the
laws that apply to you, especially for personal data (GDPR, CCPA).

**Can I schedule it or get results by webhook?** Yes. Use Scrapely schedules and webhooks, or n8n, Make and Zapier.

## Looking for an alternative?

Scrapely is an alternative to Apify, Bright Data, ScraperAPI, Firecrawl, Octoparse, PhantomBuster, SerpApi,
Zyte and others. See the side-by-side pricing on [scrape.ly/compare](https://scrape.ly/compare).

---

**Keywords:** trustpilot reviews scraper, trustpilot scraper, trustpilot scraper api, trustpilot scraper python, trustpilot scraper node.js,
scrape trustpilot, trustpilot data extraction, trustpilot crawler, trustpilot api, export trustpilot data to csv, trustpilot-scraper

License: MIT. Example code only; the scraper runs on [Scrapely](https://scrape.ly/store/cornerledger/trustpilot-scraper).
