__author__ = 'Maria'
# data
import numpy as np
import time

# stock_prices_yesterday = np.array([10,9,8,7,6,5])
stock_prices_yesterday = np.random.randint(1000, size=1)
stock_prices_yesterday = list(stock_prices_yesterday)
# print(stock_prices_yesterday)

# function

def get_max_profit(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_prices = [stock_prices_yesterday[0]]  # buy first
    profit = [stock_prices_yesterday[1] - min_prices[0]]   # first profit = sell - buy(min)

    for price in stock_prices_yesterday[1:]:
        if (price - min_prices[-1]) > profit[-1]:
            profit.append(price - min_prices[-1])
            # print("price - min_prices[-1]: ",price, min_prices[-1], price - min_prices[-1])
        elif price < min_prices[-1]:
            min_prices.append(price)
            # print("min_prices.append(price): ", min_prices)
    # print(profit)
    return profit[-1]


start = time.time()
print("Best profit: ", get_max_profit(stock_prices_yesterday))
end = time.time()
print("Time elapsed: ", end - start)
