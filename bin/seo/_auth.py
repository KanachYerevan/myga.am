"""Shared configuration, authentication and caching helpers for SEO reports.

Credentials are read from a read-only Google service account. The key file
defaults to ``.secrets/ga4-sa.json`` (gitignored) and can be overridden with
the ``GOOGLE_APPLICATION_CREDENTIALS`` environment variable.
"""

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / "data" / "seo-cache"
DEFAULT_KEY = ROOT / ".secrets" / "ga4-sa.json"

CREDENTIALS_PATH = Path(
    os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", str(DEFAULT_KEY))
)
GA4_PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "475759852")
GSC_SITE = os.environ.get("GSC_SITE", "sc-domain:kanachyerevan.am")

GSC_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GA4_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"

# Search Console keeps roughly 16 months of data. Leave a margin for the
# processing delay (data for the last couple of days is incomplete).
GSC_MAX_DAYS = 470


def credentials(scope):
    """Return service account credentials for the given scope."""
    from google.oauth2 import service_account

    if not CREDENTIALS_PATH.exists():
        raise SystemExit(
            f"Service-account key not found: {CREDENTIALS_PATH}\n"
            "Place the JSON key there or set GOOGLE_APPLICATION_CREDENTIALS."
        )

    return service_account.Credentials.from_service_account_file(
        str(CREDENTIALS_PATH), scopes=[scope]
    )


def date_windows():
    """Named date windows shared by both data sources."""
    today = date.today()
    # GA4/GSC both lag slightly; stop two days back.
    end = today - timedelta(days=2)
    return {
        "90d": (end - timedelta(days=90), end),
        "180d": (end - timedelta(days=180), end),
        "16m": (end - timedelta(days=GSC_MAX_DAYS), end),
    }


def ensure_cache_dir():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR


def cache_path(name):
    return ensure_cache_dir() / name


def write_cache(name, payload):
    path = cache_path(name)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def read_cache(name):
    path = cache_path(name)
    if not path.exists():
        raise SystemExit(
            f"Missing cache file {path}. Run the report scripts first (`make seo`)."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def log(message):
    print(message, file=sys.stderr)
