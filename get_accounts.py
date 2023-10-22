#!/usr/bin/python3
import configparser, hashlib, hmac, json, requests, time

host = "api.coinbase.com"
url = "/api/v3/brokerage/accounts"
request_body = ''

timestamp = str(int(time.time()))

# Read API secret from config file
config = configparser.ConfigParser()
config.read('credentials.ini')
api_key = config['credentials']['api_key']
api_secret = config['credentials']['api_secret']

# Create HMAC signature used for authentication
message = timestamp + 'GET' + url + request_body
signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()

# Perform HTTP request and throw exception on errors
headers = {
    'CB-ACCESS-KEY': api_key,
    'CB-ACCESS-SIGN': signature.hex(),
    'CB-ACCESS-TIMESTAMP': timestamp
}
full_path = "https://" + host + url
response = requests.get(full_path, headers=headers)
response.raise_for_status()

print(json.dumps(response.json(), indent=4))
