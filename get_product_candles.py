#!/usr/bin/python3
import cb_api, json, sympy, time
import matplotlib.pyplot as plt

product = 'BTC-USDC'
now_ts = int(time.time())

try:
    response = cb_api.get_response(
        '/api/v3/brokerage/products/' + product + '/candles',
        {
            'start': now_ts - 7*24*60*60,
            'end': now_ts,
            'granularity': 'ONE_HOUR'
        }
    )
except:
    print(response)

data = response.json()['candles']
close_prices = list(map(lambda i: float(i['close']), data))
close_prices.reverse() # CB returns latest values first
plt.plot(close_prices)
plt.ylabel('BTC USD price')
plt.show()
