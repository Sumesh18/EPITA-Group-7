import requests
from epita_group7.config import config

def fetch_live_data(country: str) -> dict:
    config.validate()
    url = "https://newsapi.org/v2/top-headlines"
    headers = {"X-Api-Key": config.api_key}
    resp = requests.get(url, headers=headers, params={"country": country}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {
        "status": "LIVE_SUCCESS",
        "total_results": data.get("totalResults", 0),
        "articles": data.get("articles", [])
    }