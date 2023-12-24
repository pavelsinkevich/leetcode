'''You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, 
while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.'''

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero_start_change_qty, one_start_change_qty = 0, 0
        for i in range(len(s)):
            if (s[i] == '0' and i%2 == 0) or (s[i] == '1' and i%2 == 1):
                one_start_change_qty += 1
            else:
                zero_start_change_qty += 1
        return min(zero_start_change_qty, one_start_change_qty)


s = "0100"      
obj = Solution()
print(obj.minOperations(s))  