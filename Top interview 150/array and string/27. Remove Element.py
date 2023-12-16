'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.'''
nums = [0,1,2,2,3,0,4,2,0]
#nums = [2,2,2,2,2]
val = 2
'''index_to_replace = 0
replacement_index =  len(nums) - 1
good_values = 0
while index_to_replace < len(nums):
    if nums[index_to_replace] == val:
        while nums[replacement_index] == val and index_to_replace < replacement_index:
            replacement_index -= 1
        if index_to_replace < replacement_index:
            nums[index_to_replace] = nums[replacement_index]
            nums[replacement_index] = val
            replacement_index -= 1
            good_values += 1
    else:
        good_values += 1
    index_to_replace += 1
k = good_values'''
index_to_replace = 0
replacement_index =  len(nums) - 1
bad_values = 0
while index_to_replace <= replacement_index:
    if nums[index_to_replace] == val:
        while nums[replacement_index] == val and index_to_replace < replacement_index:
            replacement_index -= 1
            bad_values +=1
        if index_to_replace < replacement_index:
            nums[index_to_replace] = nums[replacement_index]
            #nums[replacement_index] = val
            replacement_index -= 1
        bad_values +=1
    index_to_replace += 1
k = len(nums) - bad_values


print(k)
print(nums)
