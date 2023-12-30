'''Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        l1 = len(board)
        l2 = len(board[0])
        #result_board = [["X"]*l2 for _ in range(l1)]
        def mark_island(i, j):
            if i < 0 or j < 0 or i >= l1 or j >= l2:
                return
            elif board[i][j] == 'X' or board[i][j] == '#':
                return
            board[i][j] = '#'
            mark_island(i+1, j)
            mark_island(i-1, j)
            mark_island(i, j+1)
            mark_island(i, j-1)
            return
        
        for i in range(l1):
            mark_island(i, 0)
            mark_island(i, l2 - 1)
        for j in range(l2):
            mark_island(0, j)
            mark_island(l1 - 1, j)
        
        for i in range(l1):
            for j in range(l2):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board
        
            
    
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj = Solution()
print(obj.solve(board))