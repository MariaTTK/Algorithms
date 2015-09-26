__author__ = 'Maria'
import numpy as np
import time
# stock_prices_yesterday = np.array([7, 6, 9, 3, 6, 1, 6, 2, 1, 7, 7, 3, 5, 8, 6, 7, 0, 9, 4, 6, 7, 5, 8, 9, 1, 3, 8, 8, 9, 0, 2, 6, 9, 9, 0, 9, 6, 4, 7, 6, 5, 2, 4, 6, 0, 6, 3, 4, 2, 1, 8, 0, 0, 1, 4, 2, 7, 5, 9, 5, 5, 0, 0, 7, 9, 5, 8, 9, 0, 2, 5, 3, 3, 5, 5, 8, 8, 3, 7, 0, 0, 7, 5, 6, 3, 3, 9, 7, 8, 9, 1, 8, 2, 4, 0, 1, 2, 8, 0, 2])
stock_prices_yesterday =np.random.randint(1000, size=5000000)
stock_prices_yesterday = list(stock_prices_yesterday)
# print(stock_prices_yesterday)

def get_max_profit(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price
        # print("current_price: ",current_price)
        # print("min_price: ",min_price)

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        # print("max_profit: ",max_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit

start = time.time()
print(get_max_profit(stock_prices_yesterday))
end = time.time()
print("Time elapsed: ",end - start)
