'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            new_index = (start_index + end_index) // 2
            if nums[new_index] == target:
                return new_index
            if nums[new_index] < target:
                start_index = new_index + 1
            else:
                end_index = new_index - 1
        return start_index
        
    
nums = [1,3,5,6]
target = 7
obj = Solution()
print(obj.searchInsert(nums, target))