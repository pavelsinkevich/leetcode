'''Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.'''

from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(level, position):
            if level + 1 == len(triangle):
                return triangle[level][position]
            else:
                left = dp(level+1, position)
                right = dp(level+1, position+1)
                return triangle[level][position] + min(left, right)
        
        return dp(0, 0)

triangle = [[-10]]
obj = Solution()
print(obj.minimumTotal(triangle))