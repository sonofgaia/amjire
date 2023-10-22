#!/usr/bin/python3
import cb_api, json

response = cb_api.get_response('/api/v3/brokerage/product_book', {'product_id': 'BTC-USDC'})

print(json.dumps(response.json(), indent=4))
