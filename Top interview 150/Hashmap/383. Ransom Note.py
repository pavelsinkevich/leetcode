'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = defaultdict(int)
        for letter in magazine:
            magazine_letters[letter] += 1
        for letter in ransomNote:
            magazine_letters[letter] -= 1
            if magazine_letters[letter] < 0:
                return False
        return True
    
ransomNote = "a"
magazine = "b"
obj = Solution()
print(obj.canConstruct(ransomNote, magazine))