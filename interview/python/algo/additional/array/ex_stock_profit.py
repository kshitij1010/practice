# Write an efficient function that takes stock_prices and
# returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
#
# stock_prices, where:
# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.
#
# Example,
# stock_prices = [10, 7, 5, 8, 11, 9]
# get_max_profit(stock_prices)
#
# Returns 6 (buying for $5 and selling for $11)
#
# Reference:
# https://www.interviewcake.com/question/python/stock-price




def get_max_profit(stock_prices):
    stock_size = len(stock_prices)

    if stock_size < 2:
        raise Exception('Not enough input')

    min_price = stock_prices[0]

    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, stock_size):
        curr_price = stock_prices[i]
        curr_profit = curr_price - min_price
        max_profit = max(max_profit, curr_profit)
        min_price = min(min_price, curr_price)

    return max_profit


print get_max_profit([1, 5, 3, 2])
# Output: 4

print get_max_profit([7, 2, 8, 9])
# Output: 7

print get_max_profit([1, 6, 7, 9])
# Output: 8

print get_max_profit([9, 7, 4, 1])
# Output: -2

print get_max_profit([1, 1, 1, 1])
# Output: 0

print get_max_profit([])
# Output: raise Exception

print get_max_profit([1])
# Output: raise Exception
