import requests
from datetime import datetime
from time import time
import pandas as pd
import matplotlib.pyplot as plt

# get timestamp date of today in seconds
now_is = int(time())
# sec  min  hour days
# print(now_is)
price_dict = {}


# def main():
#     coin_pair = "XRP-USDT"  # BTC-USDT
#     time_frame = "1hour"  # 1day 4hour 1min
#     days = 40
#     price_dict = get_pair_history(time_frame, coin_pair, days)
#     plot_price(price_dict)


def get_pair_history(coin_pair, time_frame, days_back):
    days_delta = 60 * 60 * 24 * days_back
    start_At = now_is - days_delta
    base_url = "https://api.kucoin.com"
    price_url = f"/api/v1/market/candles?type={time_frame}&symbol={coin_pair}&startAt={start_At}&endAt={now_is}"
    prices = requests.get(base_url + price_url).json()
    for item in prices['data']:
        # convert date from timestamp to Y M D
        date_converted = datetime.fromtimestamp(int(item[0])).strftime("%Y-%m-%d-%H")
        price_dict[date_converted] = item[0], item[1], item[2], item[3], item[4], item[5], item[6]
    return price_dict


def plot_price(price_dict):
    plot_dict = {}
    for each_line in price_dict:
        plot_dict[each_line] = price_dict[each_line][2]
    priceDF = pd.DataFrame(plot_dict, index=["price"]).T
    # Convert prices into a float
    priceDF['price'] = priceDF['price'].astype(float)

    # convert dates to datetime from object
    priceDF.index = pd.to_datetime(priceDF.index)

    # reverse dates
    priceDF = priceDF.iloc[::-1]
    print(priceDF)

    # moving_average 200 days(
    priceDF['200MA'] = priceDF['price'].rolling(200).mean()
    priceDF['52MA'] = priceDF['price'].rolling(52).mean()

    priceDF

    # plot

    fig, ax = plt.subplots()
    ax.plot(priceDF[['price', '200MA', '52MA']])
    # Rotate and align the tick labels so they look better.
    fig.autofmt_xdate()
    ax.legend(['price', '200MA', '52MA'])
    # Use a more precise date string for the x axis locations in the toolbar.

    plt.show()


# if __name__ == "__main__":
#     main()