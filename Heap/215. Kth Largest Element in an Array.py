'''Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?'''
from heapq import heappop
from heapq import heappush


class Solution():
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        priority_queue = []
        for num in nums:
            heappush(priority_queue, -num)
        val = -heappop(priority_queue)
        for i in range(1, k):
            val = -heappop(priority_queue)
        return val

nums = [3,2,3,1,2,4,5,5,6]
k = 4   
obj = Solution()
print(obj.findKthLargest(nums, k))
            