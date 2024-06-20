''''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s[::-1].split(" ")
        wordList = [w for w in wordList if w]
        return len(wordList[0])

s = "   fly me   to   the moon  "
obj = Solution()
print(obj.lengthOfLastWord(s))