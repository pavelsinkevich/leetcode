'''You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.'''
from collections import defaultdict


class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used_nums = defaultdict(int)
        for n in nums:
            row_number = used_nums[n]
            if len(res) < row_number + 1:
                res.append([])
            res[row_number].append(n)
            used_nums[n] += 1
        return res

        
        
nums = [1,3,4,1,2,3,1]
obj = Solution()
print(obj.findMatrix(nums))