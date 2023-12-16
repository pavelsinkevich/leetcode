'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements 
in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''
nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6] 
n = 3
'''nums1 = [0]
m = 0 
nums2 = [1]
n = 1'''

nums1_current_index = 0
nums1_current_val = 0
for i in range(n):
    #if nums1_current_index >= m:
    #    break
    insert_value = nums2[i]
    if nums1_current_index< m:
        nums1_current_val = nums1[nums1_current_index]
    while nums1_current_val < insert_value and nums1_current_index < m:
        nums1_current_index += 1
        if nums1_current_index< m:
            nums1_current_val = nums1[nums1_current_index]
    #nums1.insert(nums1_current_index, insert_value)
    if nums1_current_index + 1 < m+n:
        for j in reversed(range(nums1_current_index + 1, m+n)):
            nums1[j] = nums1[j-1]
    nums1[nums1_current_index] = insert_value
    m += 1
    nums1_current_index += 1
print(nums1)