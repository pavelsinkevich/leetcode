'''Run-length encoding is a string compression method that works by replacing consecutive identical characters 
(repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". 
Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version 
of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.'''

'''import heapq
class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters_qty = list()
        if len(s) == 0:
            return 0
        letters_qty.append([s[0], 0])

        for char in s:
            if char == letters_qty[-1][0]:
                letters_qty[-1][1] += 1
            else:
                letters_qty.append([char, 1])
        current_len = 0
        best_combinations = [] # this is a heapq

        # add new item to letters_qty[i]: if we remove this whole section, how many points we win? (1 point == 1 removed symbol)
        for i in range(len(letters_qty)):
            section_length = len(str(letters_qty[i][1])) - (1 if letters_qty[i][1]==1 else 0) + 1
            current_len += section_length
            #print(section_length)
            letters_qty[i].append(section_length)
            if i > 0 and i < len(letters_qty) - 1:
                if letters_qty[i-1][0] == letters_qty[i+1][0]:
                    section_length_left = len(str(letters_qty[i-1][1])) - (1 if letters_qty[i-1][1]==1 else 0) + 1
                    section_length_right = len(str(letters_qty[i+1][1])) - (1 if letters_qty[i+1][1]==1 else 0) + 1
                    section_length_merged = len(str(letters_qty[i-1][1] + letters_qty[i+1][1])) + 1
                    letters_qty[i][2] += max(section_length_left + section_length_right - section_length_merged, 0)
            letters_in_section = letters_qty[i][1]
            victory_points = letters_qty[i][2]
            victory_point_cost = letters_in_section / victory_points
            heapq.heappush(best_combinations, (victory_point_cost, letters_in_section, victory_points, letters_qty[i][0], i))
        #print(letters_qty)
        # now we take best combinations (with least victory_point_cost) until we reach k
        current_k = k
        #deleted_indexes = set()

        while current_k > 0:
            if len(best_combinations)>0:
                combination = heapq.heappop(best_combinations)
                current_k -=combination[1]
                if current_k >= 0:
                    current_len -=combination[2]
            else:
                current_k = 0
        return current_len'''

from functools import cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, previous_char, previous_char_qty, k):
            # set it to inf as we will take the min later
            if k < 0: return float('inf')
            # we reached the end of string. Return 0
            if i == len(s): return 0
            # here we can have two choices, we either
            # 1. delete the current char
            # 2. keep the current char
            # we calculate both result and take the min one
            delete = dp(i + 1, previous_char, previous_char_qty, k - 1)
            if s[i] == previous_char:
                # e.g. a2 -> a3
                keep = dp(i + 1, previous_char, previous_char_qty + 1, k)
                # e.g. a9 -> a10
                old_len = len(str(previous_char_qty)) if previous_char_qty != 1 else 0
                new_len = len(str(previous_char_qty + 1))
                keep += new_len - old_len
            else:
                # e.g. a -> b
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)
        
        return dp(0, "", 0, k)


s = "aaabcccd"
k = 2
obj = Solution()
print(obj.getLengthOfOptimalCompression(s, k))