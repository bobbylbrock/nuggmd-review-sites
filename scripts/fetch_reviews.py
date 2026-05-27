"""
Fetch all reviews from Google Sheet and write src/data/reviews.json.
Designed to run in CI — reads credentials from env vars.
"""

import json
import os
import sys
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SHEET_ID  = os.environ["REVIEWS_SHEET_ID"]
TAB       = "All Reviews"
OUT       = Path(__file__).parent.parent / "src" / "data" / "reviews.json"

SOURCE_TO_PLATFORM = {
    "gmb":        "Google",
    "trustpilot": "Trustpilot",
    "bbb":        "BBB",
    "facebook":   "Facebook",
}

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_creds() -> Credentials:
    token_data  = json.loads(os.environ["SHEET_TOKEN_JSON"])
    client_data = json.loads(os.environ["SHEET_CREDENTIALS_JSON"])
    client      = client_data.get("installed") or client_data.get("web")

    creds = Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=client["token_uri"],
        client_id=client["client_id"],
        client_secret=client["client_secret"],
        scopes=SCOPES,
    )
    if creds.refresh_token:
        creds.refresh(Request())
    return creds


def main():
    creds = get_creds()
    svc   = build("sheets", "v4", credentials=creds)

    result = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=f"'{TAB}'!A2:L",
    ).execute()

    rows     = result.get("values", [])
    reviews  = []
    skipped  = 0

    for row in rows:
        row += [""] * (12 - len(row))
        body    = row[0].strip()
        rating  = row[1]
        author  = row[2].strip() or "Anonymous"
        date    = row[3].strip()
        source  = row[7].strip().lower()
        loc     = row[8].strip()
        url     = row[9].strip()
        uid     = row[11].strip()

        if not body or not date:
            skipped += 1
            continue
        try:
            rating_f = float(rating)
        except (ValueError, TypeError):
            skipped += 1
            continue
        if author == "BBB Complaint":
            skipped += 1
            continue

        platform = SOURCE_TO_PLATFORM.get(source, source.capitalize())
        reviews.append({
            "id":       uid or f"{source}-{len(reviews)}",
            "body":     body,
            "rating":   rating_f,
            "author":   author,
            "date":     date,
            "platform": platform,
            "location": loc,
            "url":      url,
            "verified": True,
        })

    by_platform = {}
    for r in reviews:
        by_platform.setdefault(r["platform"], 0)
        by_platform[r["platform"]] += 1

    print(f"Fetched {len(rows)} rows — {len(reviews)} reviews, {skipped} skipped")
    for plat, cnt in sorted(by_platform.items()):
        print(f"  {plat}: {cnt}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(reviews, f, indent=2)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
