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