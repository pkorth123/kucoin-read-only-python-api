from kucoin.client import Client


api_passphrase = 'SlackPack83'
api_key  = '61b930a39927ba00018cf593'
api_secret = 'c99f9126-12e5-4fa2-9d94-472df4d22f33'
client = Client(api_key, api_secret, api_passphrase)


def main():
    print(client.get_ticker('BTC-USDT')['price'])

if __name__ == "__main__":
    main()