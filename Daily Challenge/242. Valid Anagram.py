'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''
s = "anagram"
t = "nagaram"
s_dict = dict()
for letter in s:
    if letter not in s_dict:
        s_dict[letter] = 1
    else:
        s_dict[letter] += 1
t_dict = dict()
for letter in t:
    if letter not in t_dict:
        t_dict[letter] = 1
    else:
        t_dict[letter] += 1
is_anagram = (s_dict == t_dict)
print(is_anagram)