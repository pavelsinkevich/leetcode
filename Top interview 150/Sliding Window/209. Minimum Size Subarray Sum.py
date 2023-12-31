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
# this solution works

'''class Solution(object):
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
                min_len = min(min_len, end_index - start_index + 1)
                current_sum -= nums[start_index]
                start_index +=1
            end_index += 1
            if end_index == len_nums:
                return min_len
            current_sum += nums[end_index]'''

# use binary search to make it faster             
# note: it is actually slower then previous one
class Solution(object):
    def isGoodListOfSpecificLengthExist(self, target, nums, len_nums, specific_length):
        start_index = 0
        end_index = 0
        current_sum = nums[start_index]
        if current_sum >= target:
                return True
        while end_index < len_nums - 1:
            end_index += 1
            current_sum += nums[end_index]
            if end_index - start_index + 1 > specific_length:
                current_sum -= nums[start_index]
                start_index += 1
            if current_sum >= target:
                return True
        return False



    def minSubArrayLen(self, target, nums):
        total_sum = sum(nums)
        len_nums = len(nums)
        if total_sum == target:
            return len_nums
        if total_sum < target:
            return 0
        min_len = 1
        max_len = len_nums
        best_len = len_nums
        while min_len <= max_len:
            mid = (min_len + max_len) // 2
            if self.isGoodListOfSpecificLengthExist(target, nums, len_nums, mid):
                best_len = mid
                max_len = mid - 1
            else:
                min_len = mid + 1
        return best_len


target = 6
nums = [10,2,3]
obj = Solution()           
print(obj.minSubArrayLen(target, nums))