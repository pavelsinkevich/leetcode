'''Run-length encoding is a string compression method that works by replacing consecutive identical characters 
(repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". 
Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version 
of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.'''
import heapq


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
                #print(combination)
                #combination_index = combination[4]
                #print(combination_index)
                #if not combination_index+1 in deleted_indexes and not combination_index-1 in deleted_indexes:
                #if combination_index in deleted_indexes:
                    #deleted_indexes.add(combination_index)
                current_k -=combination[1]
                if current_k >= 0:
                    current_len -=combination[2]
            else:
                current_k = 0
        return current_len
        #return [heapq.heappop(best_combinations) for i in range(len(best_combinations))]

s = "aabaabbcbbbaccc"
k = 6
obj = Solution()
print(obj.getLengthOfOptimalCompression(s, k))