'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for w in strs:
                if len(w) <= i:
                    return strs[0][0:i]
                elif w[i] != strs[0][i]:
                    return strs[0][0:i]
        return strs[0]

'''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs.sort()
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][0:i]
        return strs[0]'''

obj = Solution()
strs = ["ab", "a"]
print(obj.longestCommonPrefix(strs))