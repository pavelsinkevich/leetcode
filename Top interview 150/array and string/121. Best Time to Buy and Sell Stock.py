'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''
prices = [7,1,5,3,6,4]
'''
max_profit = 0
if prices: #True if not empty
    min_price = prices[0]
    for price in prices:
        if price - min_price > max_profit:
            max_profit = price - min_price
        if price < min_price:
            min_price = price
print(max_profit)'''


max_profit = 0
if prices: #True if not empty
    min_price_index = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[min_price_index] > max_profit:
            max_profit = prices[i] - prices[min_price_index]
        if prices[i] < prices[min_price_index]:
            min_price_index = i
print(max_profit)