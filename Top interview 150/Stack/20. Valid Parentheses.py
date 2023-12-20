'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s_list = [s[0]]
        for letter in s[1:]:
            prev_letter = ''
            if len(s_list) != 0:
                prev_letter = s_list[-1]
            if (letter == ']' and prev_letter != '[') or (letter == ')' and prev_letter != '(') or (letter == '}' and prev_letter != '{'):
                return False
            elif (letter == ']' and prev_letter == '[') or (letter == ')' and prev_letter == '(') or (letter == '}' and prev_letter == '{'):
                #del s_list[-1]
                s_list.pop()
            else:
                s_list.append(letter)
        return len(s_list) == 0
        

        
s = "()"
obj = Solution()
print(obj.isValid(s))        