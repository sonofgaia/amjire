#!/usr/bin/python3
import cb_api, json

response = cb_api.get_response('/api/v3/brokerage/orders/historical/batch', {'product_id': 'BTC-USDC', 'order_status': 'OPEN'})

print(json.dumps(response.json(), indent=4))
