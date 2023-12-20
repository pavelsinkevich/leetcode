'''You are given an integer array prices representing the prices of various chocolates in a store. 
You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. 
You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. 
If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.'''
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if money - prices[0] - prices[1] >= 0:
            return money - prices[0] - prices[1]
        else:
            return money

prices = [1,2,2]
money = 3        
obj = Solution()
print(obj.buyChoco(prices, money))