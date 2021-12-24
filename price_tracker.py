import os
import metatrader
from kucoin.client import Client
import queue

from get_historical_data import get_pair_history, plot_price


# don't really need api access to account unless actively trading
# api_passphrase = os.environ['KUCOIN_API_PASSPHRASE_READ_ONLY']
# api_key  = os.environ['KUCOIN_API_KEY_READ_ONLY']
# api_secret = os.environ['KUCOIN_API_SECRET_READ_ONLY']
# client = Client(api_key, api_secret, api_passphrase)


def main():
    # '1hour', '1day', '4hour', or '1min'
    time_frame = "1hour"
    coin_pair = 'BTC-USDT'
    days_back = 40
    backtest_market(coin_pair, time_frame, days_back)


def backtest_market(coin_pair, time_frame, days_back):
    data = get_pair_history(coin_pair, time_frame, days_back)
    backtest_donchian(data)
    # plot_price(data)


def backtest_donchian(data, period=20):
    get_donchian_channels(data, period)


def get_donchian_channels(data, period):
    donchian_channel = []
    highs_q = queue.Queue(period)
    lows_q = queue.Queue(period)
    i = 0
    for candle in data:
        i += 1
        high = data[candle][3]
        low = data[candle][4]
        highs_q.put(high)
        lows_q.put(low)
        if highs_q.full():
            highest_high, lowest_low = get_donchian_vals(highs_q, lows_q)
            highs_q.get()
            lows_q.get()
            middle_channel = (highest_high + lowest_low)/2
            donchian_channel.append((highest_high, lowest_low, middle_channel))
    for donchian_vals in donchian_channel:
        print(donchian_vals)


# get donchian high channel, low channel and middle channel for a given period represented by queues of length {period}
def get_donchian_vals(highs_q, lows_q):
    # highs = list(highs_q)
    # lows = list(lows_q)
    highest_high = 0
    lowest_low = 1000000
    for i in range(len(highs_q.queue)):
        high_val = float(highs_q.queue[i])
        low_val = float(lows_q.queue[i])
        if float(high_val > highest_high):
            highest_high = high_val
        if float(low_val < lowest_low):
            lowest_low = low_val
    return highest_high, lowest_low


if __name__ == "__main__":
    main()
