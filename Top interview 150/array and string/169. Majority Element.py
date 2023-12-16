'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''
nums = [3,2,3]
res_dict = dict()
l = len(nums)
for i in nums:
    if i not in res_dict:
        res_dict[i] = 1
    else:
        res_dict[i] += 1
    if res_dict[i] >= -(-l // 2):
        print(i)

