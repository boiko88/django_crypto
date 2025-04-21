from django.core.cache import cache
from django.conf import settings as conf_settings
import requests


def crypto_rates(request):
    # Check if cached data exists
    cached_data = cache.get("crypto_rates")
    if cached_data:
        return {"crypto_rates": cached_data}

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": conf_settings.COINMARKETCAP_KEY}

    try:
        session = requests.Session()
        session.headers.update(headers)

        crypto_data = {}

        # Bitcoin
        btc_params = {"slug": "bitcoin", "convert": "USD"}
        btc_response = session.get(url, params=btc_params).json()
        if "data" in btc_response and "1" in btc_response["data"]:
            crypto_data["bitcoin"] = round(btc_response["data"]["1"]["quote"]["USD"]["price"], 1)

        # Ethereum
        eth_params = {"slug": "ethereum", "convert": "USD"}
        eth_response = session.get(url, params=eth_params).json()
        if "data" in eth_response and "1027" in eth_response["data"]:
            crypto_data["ethereum"] = round(eth_response["data"]["1027"]["quote"]["USD"]["price"], 1)

        # Store in cache for 5 minutes
        cache.set("crypto_rates", crypto_data, timeout=300)

        return {"crypto_rates": crypto_data}

    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return {"crypto_rates": None}