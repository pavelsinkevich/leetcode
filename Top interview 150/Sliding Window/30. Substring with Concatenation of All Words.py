'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.'''

from collections import defaultdict
from typing import List


class Solution:
    def isConcat(self, s:str, word_dict: defaultdict[str], word_len) -> bool:
        substring_word_dict = defaultdict(lambda: 0)
        for i in range(0, len(s), word_len):
            substring_word_dict[s[i:i+word_len]] += 1
        return word_dict == substring_word_dict

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dict = defaultdict(lambda: 0)
        for w in words:
            word_dict[w] += 1
        word_len = len(words[0])
        concat_len = word_len * len(words)
        left = 0
        res = []
        while left <= len(s) - concat_len:
            currentSubstring = s[left:left+concat_len]
            if self.isConcat(currentSubstring, word_dict, word_len):
                res.append(left)
            left += 1
        return res

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
obj = Solution()
print(obj.findSubstring(s, words))