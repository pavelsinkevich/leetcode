'''A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above 
(there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.'''

# Time Limit Exceeded. Too slow
'''class Solution(object):
    def __init__(self):
        self.letter_codes = set()
        for i in range(1, 27):
            self.letter_codes.add(str(i))
        self.ways_qty = 0
    
    def decodePart(self, s):
        l = len(s)
        if len(s) > 0:
            if s[0] in self.letter_codes:
                self.decodePart(s[1:])
        if len(s) >1:
            if s[0:2] in self.letter_codes:
                self.decodePart(s[2:])
        if len(s) == 0:
            self.ways_qty += 1
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.decodePart(s)
        return self.ways_qty'''
        

'''class Solution(object):
    # how many new decoding appear when we add string s2 (always 1 char) to string s1?
    def numAdditionalDecoding(self, s1, s2):
        additional_decodings = 0
        if s2 != '0':
            additional_decodings +=1
        if s1[-1] != '|' and s2 != '|':
            if s2 != '0' and 10 <= int(s1[-1] + s2) <27:
                additional_decodings +=1
        if s2 == '0' and s1[-1] != '1' and s1[-1] != '2':
            raise Exception("string cannot be decoded")
        return additional_decodings - 1
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1 and s[0] != '0':
            return 1
        s1 = ""
        # remove all '0' with leading numbers, because it's always 1 decoding
        for i in range(len(s)):
            if (s+'1')[i+1] == 0 and s[i] != '1' and s[i] != '2':
                return 0
            if s[i] != '0' and (s+'1')[i+1] != '0':
                s1 += s[i]
            else:
                s1 += '|'
        #print(s1)
        try:
            decodings = 1
            for i in range(1, len(s1)):
                decodings += self.numAdditionalDecoding(s1[:i], s1[i])
        except Exception as er:
            print(er)
            return 0

        return decodings'''
from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.letter_codes = set()
        for i in range(1, 27):
            self.letter_codes.add(str(i))
        self.ways_to_substring = defaultdict(int)
    
    def decodePart(self, s):
        if len(s) >1:
            left = s[0:2]
            right = s[2:]
            if left == "00":
                raise Exception("string cannot be decoded")
            if left in self.letter_codes:
                self.ways_to_substring[right] += self.ways_to_substring[s]
        if len(s) > 0:
            left = s[0]
            right = s[1:]
            if left in self.letter_codes:
                self.ways_to_substring[right] += self.ways_to_substring[s]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1 and s[0] != '0':
            return 1
        self.ways_to_substring[s] = 1
        try:
            for i in range(len(s)):
                self.decodePart(s[i:])
            return self.ways_to_substring[""]
        except:
            return 0

#s = "111111111111111111111111111111111111111111111"
#s = "2101" #1
#s = "12" #2
#s = "06" #0
#s = "10" #1
s = "10011"
obj = Solution()
print(obj.numDecodings(s))
