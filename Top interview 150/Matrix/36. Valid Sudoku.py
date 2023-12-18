'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.'''
import numpy as np
class Solution():
    def isValidSubSet(self, subset):
        items = dict()
        for element in subset:
            if element != ".":
                if element in items:
                    return False
                else:
                    items[element] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        np_array = np.array(board)
        # Validate rows
        for i in range(9):
            subset = np_array[i]
            if not self.isValidSubSet(subset):
                return False
        # Validate columns
        np_array = np.array(board).transpose()
        for i in range(9):
            subset = np_array[i]
            if not self.isValidSubSet(subset):
                return False
        # Validate 3x3 subarrays
        for i in range(3):
            for j in range(3):
                # Extract a 3x3 subarray from the specified position
                subset = np_array[i*3:i*3 + 3, j*3:j*3 + 3].flatten()
                if not self.isValidSubSet(subset):
                    return False
        return True
        
obj = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(obj.isValidSudoku(board))