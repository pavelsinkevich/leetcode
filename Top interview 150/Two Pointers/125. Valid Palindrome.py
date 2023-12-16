'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''
s = "A man, a plan, a canal: Panama"
s = ''.join(char.lower() for char in s if char.isalnum())
res = True
l = len(s)
for i in range(l//2):
    if s[i] != s[l-i-1]:
        res = False
print(res)