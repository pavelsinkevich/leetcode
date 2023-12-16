'''Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

# this solution works if we can skip elements of the list
# but apparently we cannot
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        total_sum = sum(nums)
        if total_sum == target:
            return len(nums)
        if total_sum < target:
            return 0
        nums.sort()
        #print(nums)
        min_len = 0
        current_sum = 0
        for i in reversed(range(len(nums))):
            current_val = nums[i]
            current_sum += nums[i]
            min_len += 1
            if current_sum >= target:
                return min_len
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        total_sum = sum(nums)
        len_nums = len(nums)
        if total_sum == target:
            return len_nums
        if total_sum < target:
            return 0
        min_len = len_nums
        start_index = 0
        current_sum = nums[start_index]
        end_index = 0
        while end_index < len_nums:
            while current_sum >= target:
                if end_index - start_index + 1 < min_len:
                    min_len = end_index - start_index + 1
                current_sum -= nums[start_index]
                start_index +=1
            end_index += 1
            if end_index == len_nums:
                return min_len
            current_sum += nums[end_index]
                



target = 7
nums = [2,3,1,2,4,3]  
obj = Solution()           
print(obj.minSubArrayLen(target, nums))