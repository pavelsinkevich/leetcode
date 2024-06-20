'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and 
(i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.'''
from typing import List


'''class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                currentArea = min(height[i], height[j]) * (j - i)
                currentMax = max(currentMax, currentArea)
        return currentMax'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax = 0
        left = 0
        right = len(height)-1
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            currentMax = max(currentMax, currentArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return currentMax


height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))
