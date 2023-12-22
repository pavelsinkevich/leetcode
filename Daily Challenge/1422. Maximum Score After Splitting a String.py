'''Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings 
(i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.'''
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero_count_left = 0
        ones_count_right = len(s.replace('0', ''))
        max_score = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count_left += 1
            else:
                ones_count_right -= 1
            max_score = max(max_score, zero_count_left + ones_count_right)
        return max_score
s = "00"
obj = Solution()
print(obj.maxScore(s))        