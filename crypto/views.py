from django.views.generic import TemplateView
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from crypto.context_processors import crypto_rates


class CryptoPageView(LoginRequiredMixin, TemplateView):
    template_name: str = "crypto.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context: dict[str, any] = super().get_context_data(**kwargs)

        # Ensure CoinMarketCap data is included (otherwise navbar will be empty)
        context.update(crypto_rates(self.request))

        # Check if Bybit data is in cache
        cached_data: dict[str, float] | None = cache.get("bybit_crypto_data")
        if cached_data:
            context["bybit_crypto_rates"] = cached_data
            return context

        url: str = "https://api.bybit.com/v5/market/tickers?category=spot"

        try:
            response = requests.get(url)
            data: dict[str, any] = response.json()

            if "result" in data and "list" in data["result"]:
                tickers: list[dict[str, any]] = data["result"]["list"]
                crypto_data: dict[str, float] = {}

                # Filter for required cryptocurrencies
                coins: dict[str, str] = {
                    "BTCUSDT": "Bitcoin",
                    "ETHUSDT": "Ethereum",
                    "TONUSDT": "TON",
                    "SOLUSDT": "Solana",
                    "XRPUSDT": "XRP",
                    "BNBUSDT": "BNB",
                    "ADAUSDT": "Cardano",
                    "DOGEUSDT": "Dogecoin",
                }

                for ticker in tickers:
                    symbol: str = ticker["symbol"]
                    if symbol in coins:
                        crypto_data[coins[symbol]] = round(float(ticker["lastPrice"]), 2)

                # Cache the data for 5 minutes
                cache.set("bybit_crypto_data", crypto_data, timeout=300)
                context["bybit_crypto_rates"] = crypto_data
            else:
                context["bybit_crypto_rates"] = None

        except Exception as e:
            print(f"Error fetching Bybit data: {e}")
            context["bybit_crypto_rates"] = None

        return context


class HomePageView(TemplateView):
    template_name: str = 'home.html'
