import pprint
from requests import Request, Session
import json

COIN_API = 'bd76f1a8-3785-4c57-8799-1f0320cb8ccd'

def gst_price(coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': coin,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COIN_API
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    r = json.loads(response.text)['data']['GST']['quote']['USD']['price']
    b = f"GST price is: {str(round(r, 5))}"
    return b


print(gst_price('GST'))