# kucoin-read-only-python-api
With the idea of eventually creating a trading bot, the goal of THIS code is to be given the ticker of a given asset and automatically backtest all trading strategies coded for in multiple time frames with several parameter variations iterated over. Once this process is complete the user will receive a report of the asset they inquired about indicating the most profitable trading strategy with the suggested input timeframe and period.

STRATEGIES:
Donchian - Currently the code is able to pull an input range of data from an input asset and identify a Donchian breakout in that data.
