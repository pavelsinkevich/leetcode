'''You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any 
position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.'''
from collections import defaultdict


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        letter_dict = defaultdict(int)
        for word in words:
            for char in word:
                letter_dict[char] += 1
        l = len(words)
        for letter in letter_dict:
            if letter_dict[letter] % l != 0:
                return False
        return True




words = ["abc","aabc","bc"]
obj = Solution()
print(obj.makeEqual(words))