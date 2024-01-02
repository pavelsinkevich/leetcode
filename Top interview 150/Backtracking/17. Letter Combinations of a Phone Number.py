'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digits_to_letters = dict()
        digits_to_letters['2'] = ['a', 'b', 'c']
        digits_to_letters['3'] = ['d', 'e', 'f']
        digits_to_letters['4'] = ['g', 'h', 'i']
        digits_to_letters['5'] = ['j', 'k', 'l']
        digits_to_letters['6'] = ['m', 'n', 'o']
        digits_to_letters['7'] = ['p', 'q', 'r', 's']
        digits_to_letters['8'] = ['t', 'u', 'v']
        digits_to_letters['9'] = ['w', 'x', 'y', 'z']

        result_list = ['']
        start_index = 0
        end_index = 0

        for digit in digits:
            for letter in digits_to_letters[digit]:
                i = start_index
                while i <= end_index:
                    result_list.append(result_list[i] + letter)
                    i += 1
            start_index = end_index + 1
            end_index = len(result_list) - 1
        return result_list[start_index:]
        
digits = "23"
obj = Solution()
print(obj.letterCombinations(digits))