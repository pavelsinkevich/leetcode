'''Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?'''
#from heapq import heappop
#from heapq import heappush
import heapq


class Solution():
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]

nums = [3,2,3,1,2,4,5,5,6]
k = 4   
obj = Solution()
print(obj.findKthLargest(nums, k))
            