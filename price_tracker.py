import os

from kucoin.client import Client


api_passphrase = os.environ['KUCOIN_API_PASSPHRASE_READ_ONLY']
api_key  = os.environ['KUCOIN_API_KEY_READ_ONLY']
api_secret = os.environ['KUCOIN_API_SECRET_READ_ONLY']
client = Client(api_key, api_secret, api_passphrase)

currency = 'BTC-USDT'

def main():
    print(client.get_24hr_stats(currency))
    print(client.get_ticker(currency)['price'])

if __name__ == "__main__":
    main()