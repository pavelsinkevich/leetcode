'''The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs 
(nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.'''

# slow solution. Time Limit Exceeded
'''class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        product_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product_list.append((nums[i]*nums[j], i, j))
        max_difference = 0
        for i in range(len(product_list)):
            for j in range(i+1, len(product_list)):
                if product_list[i][1] != product_list[j][1] and \
                    product_list[i][2] != product_list[j][2] and \
                    product_list[i][1] != product_list[j][2] and \
                    product_list[i][2] != product_list[j][1]:
                    max_difference = max(max_difference, abs(product_list[i][0] - product_list[j][0]))
        return max_difference'''

# this solution is bad because I didn't notice the constraint: all nums are non negative
# so this solution adds a lot of unnesessary complexity
'''class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        nums_negative = []
        nums_positive = []
        len_positive = 0
        for i in range(len_nums):
            if (nums[i] >= 0):
                nums_positive.append(nums[i])
                len_positive += 1
            else:
                nums_negative.append(nums[i])
        nums_positive.sort()
        nums_negative.sort()
        # find biggest product: 2 biggest positives or 2 biggest negatives
        max_positive_product = float('-inf')
        max_negative_product = float('-inf')
        if len_positive > 1:
            max_positive_product = nums_positive[len_positive-1]*nums_positive[len_positive-2]
        if len_nums - len_positive > 1:
            max_negative_product = nums_negative[0]*nums_negative[1]
        max_product = max(max_positive_product, max_negative_product)
        # find smallest product: 2 smallest positives or biggest positive*biggest negative
        two_smallest_positives = float('inf')
        if len_positive > 1:
            two_smallest_positives = nums_positive[0]*nums_positive[1]
        biggest_positive_biggest_negative = float('inf')
        if len_positive > 0 and len_nums - len_positive > 0:
            biggest_positive_biggest_negative = nums_positive[len_positive-1]*nums_negative[0]
        min_product = min(two_smallest_positives, biggest_positive_biggest_negative)
        return max_product - min_product'''

# Since we know that all nums are non negative, we can take 2 smallest and 2 biggest and this will be the result
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        min_product = nums[0]*nums[1]
        max_product = nums[l-1]*nums[l-2]
        return max_product - min_product

nums = [5,6,2,7,4]
obj = Solution()           
print(obj.maxProductDifference(nums))        