'''You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges 
but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b'''
class Solution(object):
    def getRangeName(self, current_range):
        if len(current_range) == 1:
            return str(current_range[0])
        else:
            return str(current_range[0]) + '->' + str(current_range[-1])

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        ranges_list = []
        current_range = [nums[0]]
        #current_range.append(nums[0])
        for i in range(1, len(nums)):
            if current_range[-1] == nums[i] - 1:
                current_range.append(nums[i])
            else:
                ranges_list.append(self.getRangeName(current_range))
                del current_range[:]
                current_range.append(nums[i])
        ranges_list.append(self.getRangeName(current_range))
        return ranges_list

nums = [0,1,2,4,5,7]        
obj = Solution()
print(obj.summaryRanges(nums))
