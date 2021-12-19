import os
import metatrader
from kucoin.client import Client


api_passphrase = os.environ['KUCOIN_API_PASSPHRASE_READ_ONLY']
api_key  = os.environ['KUCOIN_API_KEY_READ_ONLY']
api_secret = os.environ['KUCOIN_API_SECRET_READ_ONLY']
client = Client(api_key, api_secret, api_passphrase)

currency = 'BTC-USDT'


def main():
    btc_daily_data_path = os.path.join(os.path.dirname(__file__), 'backtesting-data/btc_11-18-2020_12-18-2020.csv')
    with open(btc_daily_data_path) as csv:
        btc_daily_data = csv.readlines()
    for day in btc_daily_data:
        if day[2] == "D":
            continue
        else:
            date = day.split('\",\"')[0]
            price = day.split('\",\"')[1]
            daily_open = day.split('\",\"')[2]
            daily_high = day.split('\",\"')[3]
            daily_low = day.split('\",\"')[4]
            daily_volume = day.split('\",\"')[5]
            daily_change_percent = day.split('\",\"')[6]
    # print(client.get_24hr_stats(currency))
    # print(client.get_ticker(currency)['price'])
    # client.get_trade_histories(currency)

if __name__ == "__main__":
    main()