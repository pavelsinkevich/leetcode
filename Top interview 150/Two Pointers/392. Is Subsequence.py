'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''
s = "abc"
t = "ahbgdc"
s_current_index = 0
t_current_index = 0
while s_current_index < len(s) and t_current_index < len(t):
    if t[t_current_index] == s[s_current_index]:
        s_current_index += 1
    t_current_index += 1
print(s_current_index == len(s))
    