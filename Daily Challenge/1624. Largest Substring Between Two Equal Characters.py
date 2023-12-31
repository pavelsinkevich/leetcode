'''Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. 
If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.'''
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_min_position = dict()
        current_max_length = -1
        for i in range(len(s)):
            if not s[i] in char_min_position:
                char_min_position[s[i]] = i
            else:
                current_max_length = max(current_max_length, i - char_min_position[s[i]] - 1)
        return current_max_length
        
    
        
s = "abca"
obj = Solution()
print(obj.maxLengthBetweenEqualCharacters(s))