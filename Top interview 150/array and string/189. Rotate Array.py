'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''
nums = [-1,-100,3,99]
k = 2


'''
l = len(nums)
nums_result = []
if k != 0:
    for i in range(l):
        replace_index = (i - k + l) % l
        nums_result.append(nums[replace_index])

print(nums)
print(nums_result)
'''
l = len(nums)
replaced_indexes = set()
if k != 0 and l != 0:
    current_index = (k + l) % l
    replace_value = nums[0]
    for i in range(l):
        current_value = nums[current_index]
        nums[current_index] = replace_value
        replaced_indexes.add(current_index)
        replace_value = current_value
        current_index = (current_index + k) % l
        while current_index in replaced_indexes and i != l-1:
            current_index = (current_index + 1) % l
            replace_value = nums[(current_index - k + l) % l]
        #replace_index = (current_index + k) % l
print(nums)