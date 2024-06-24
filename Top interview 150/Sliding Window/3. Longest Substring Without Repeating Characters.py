'''Given a string s, find the length of the longest substring without repeating characters.'''
'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length_list = [0] * len(s)
        substring_letters = [set() for x in range(len(s))]
        duplicate_found = [False] * len(s)
        for i in range(len(s)):
            substring_letters[i].add(s[i])
            length_list[i] += 1
            for j in range(i):
                if not duplicate_found[j]:
                    if s[i] in substring_letters[j]:
                        duplicate_found[j] = True
                    else:
                        substring_letters[j].add(s[i])
                        length_list[j] += 1


        return max(length_list)'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        startIndex = 0
        endIndex = 0
        substringLetters = set()
        for endIndex in range(len(s)):
            if s[endIndex] not in substringLetters:
                maxLen = max(maxLen, endIndex - startIndex + 1)
            else:
                while s[endIndex] in substringLetters:
                    substringLetters.remove(s[startIndex])
                    startIndex += 1
            substringLetters.add(s[endIndex])
        return maxLen


                

s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))