"""Trustpilot Reviews Scraper with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "startUrls": [
            "https://www.trustpilot.com/review/www.bankfive.com"
        ],
        "maxReviews": 10,
        "sortBy": "recent",
        "sampling": "recent",
        "scrapeAllReviews": True,
        "filterDateRange": "all",
        "filterVerifiedOnly": False,
        "filterRepliesOnly": False,
        "strictNameMatch": False,
        "includeCompanyDetails": False,
        "includeStats": False,
        "proxyConfiguration": {
            "useScrapelyProxy": True,
            "scrapelyProxyGroups": [
                "DATACENTER"
            ]
        }
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('cornerledger/trustpilot-scraper').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
