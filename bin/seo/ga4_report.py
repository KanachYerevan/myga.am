#!/usr/bin/env python3
"""Pull Google Analytics 4 data into a local JSON cache.

Usage:
    python bin/seo/ga4_report.py
"""

from datetime import date, timedelta

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from google.api_core.exceptions import GoogleAPIError

from _auth import GA4_PROPERTY_ID, GA4_SCOPE, credentials, date_windows, log, write_cache

REPORTS = {
    "channel": (
        ["sessionDefaultChannelGroup"],
        ["sessions", "totalUsers", "engagementRate", "averageSessionDuration"],
    ),
    "landing": (
        ["landingPagePlusQueryString", "sessionDefaultChannelGroup"],
        ["sessions", "totalUsers", "engagementRate"],
    ),
    "page": (
        ["pagePath", "pageTitle"],
        ["screenPageViews", "sessions", "engagementRate", "averageSessionDuration"],
    ),
    "language": (["language"], ["sessions", "totalUsers", "engagementRate"]),
    "country": (["country"], ["sessions", "totalUsers"]),
    "device": (["deviceCategory"], ["sessions", "totalUsers", "engagementRate"]),
    "source_medium": (["sessionSourceMedium"], ["sessions", "totalUsers"]),
}

PAGE_SIZE = 100000


def ga4_windows():
    """GA4 standard properties keep ~14 months of event data."""
    today = date.today()
    end = today - timedelta(days=2)
    return {
        "90d": (end - timedelta(days=90), end),
        "365d": (end - timedelta(days=365), end),
    }


def run(client, dimensions, metrics, start, end):
    rows = []
    offset = 0
    while True:
        request = RunReportRequest(
            property=f"properties/{GA4_PROPERTY_ID}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            dimensions=[Dimension(name=d) for d in dimensions],
            metrics=[Metric(name=m) for m in metrics],
            limit=PAGE_SIZE,
            offset=offset,
        )
        response = client.run_report(request)
        for row in response.rows:
            record = {
                dim: value.value for dim, value in zip(dimensions, row.dimension_values)
            }
            for metric, value in zip(metrics, row.metric_values):
                record[metric] = value.value
            rows.append(record)
        if len(response.rows) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    return rows


def main():
    client = BetaAnalyticsDataClient(credentials=credentials(GA4_SCOPE))
    log(f"GA4 property: {GA4_PROPERTY_ID}")

    payload = {"property_id": GA4_PROPERTY_ID, "windows": {}}
    for window, (start, end) in ga4_windows().items():
        log(f"  window {window}: {start} .. {end}")
        payload["windows"][window] = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "data": {},
        }
        for name, (dimensions, metrics) in REPORTS.items():
            try:
                rows = run(client, dimensions, metrics, start, end)
            except GoogleAPIError as error:
                log(f"    {name}: FAILED ({error})")
                payload["windows"][window]["data"][name] = []
                continue
            payload["windows"][window]["data"][name] = rows
            log(f"    {name}: {len(rows)} rows")

    path = write_cache("ga4.json", payload)
    log(f"Wrote {path}")


if __name__ == "__main__":
    main()
