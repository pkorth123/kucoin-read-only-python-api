from kucoin.client import Client


api_passphrase = ''
api_key  = ''
api_secret = ''
client = Client(api_key, api_secret, api_passphrase)


def main():
    print(client.get_ticker('BTC-USDT')['price'])

if __name__ == "__main__":
    main()