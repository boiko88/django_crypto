import requests
from django.conf import settings

def get_crypto_price(symbol: str) -> float | None:
    '''
    Get current price for a cryptocurrency from CoinMarketCap API
    '''
    try:
        url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}'
        headers = {
            'X-CMC_PRO_API_KEY': settings.COINMARKETCAP_KEY,
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if response.status_code == 200 and 'data' in data:
            return float(data['data'][symbol]['quote']['USD']['price'])
        return None
    except Exception as e:
        print(f'Error fetching price for {symbol}: {str(e)}')
        return None 