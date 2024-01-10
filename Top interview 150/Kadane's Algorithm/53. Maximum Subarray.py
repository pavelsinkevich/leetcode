'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -float('inf')
        largest_item = -float('inf')
        for num in nums:
            current_sum += num
            max_sum = max(current_sum, max_sum)
            largest_item = max(largest_item, num)

            if current_sum < 0:
                current_sum = 0
        if largest_item > max_sum:
            max_sum = largest_item
        return max_sum
    
obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray(nums))
