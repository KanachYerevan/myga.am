#!/usr/bin/env python3
"""Pull Google Search Console Search Analytics data into a local JSON cache.

Usage:
    python bin/seo/gsc_report.py
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from _auth import GSC_SCOPE, GSC_SITE, credentials, date_windows, log, write_cache

DIMENSION_SETS = {
    "queries": ["query"],
    "pages": ["page"],
    "query_page": ["query", "page"],
    "daily": ["date"],
    "country_device": ["country", "device"],
}

ROW_LIMIT = 25000


def service():
    return build("searchconsole", "v1", credentials=credentials(GSC_SCOPE))


def query_all(client, dimensions, start, end):
    """Page through a Search Analytics query until all rows are collected."""
    rows = []
    start_row = 0
    while True:
        body = {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "dimensions": dimensions,
            "rowLimit": ROW_LIMIT,
            "startRow": start_row,
            "type": "web",
        }
        response = (
            client.searchanalytics().query(siteUrl=GSC_SITE, body=body).execute()
        )
        batch = response.get("rows", [])
        rows.extend(batch)
        if len(batch) < ROW_LIMIT:
            break
        start_row += ROW_LIMIT
    return rows


def simplify(rows, dimensions):
    out = []
    for row in rows:
        record = {dim: key for dim, key in zip(dimensions, row.get("keys", []))}
        record["clicks"] = row.get("clicks", 0)
        record["impressions"] = row.get("impressions", 0)
        record["ctr"] = row.get("ctr", 0)
        record["position"] = row.get("position", 0)
        out.append(record)
    return out


def main():
    client = service()

    log(f"Search Console property: {GSC_SITE}")
    try:
        sites = client.sites().list().execute().get("siteEntry", [])
    except HttpError as error:
        raise SystemExit(f"GSC access failed: {error}") from error

    log("  accessible properties: " + ", ".join(s.get("siteUrl", "?") for s in sites))

    payload = {"site": GSC_SITE, "windows": {}}
    for window, (start, end) in date_windows().items():
        log(f"  window {window}: {start} .. {end}")
        payload["windows"][window] = {"start": start.isoformat(), "end": end.isoformat(), "data": {}}
        for name, dimensions in DIMENSION_SETS.items():
            rows = query_all(client, dimensions, start, end)
            payload["windows"][window]["data"][name] = simplify(rows, dimensions)
            log(f"    {name}: {len(rows)} rows")

    path = write_cache("gsc.json", payload)
    log(f"Wrote {path}")


if __name__ == "__main__":
    main()
