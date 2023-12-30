'''You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style 
starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, 
regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder 
is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start 
of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. 
You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, 
return -1.'''
from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        l = len(board)
        board_as_line = []
        for i in range(l-1, -1, -1):
            if i%2 == (l-1)%2:
                board_as_line += board[i]
            else:
                board_as_line += reversed(board[i])
        #print(board_as_line)
        #for i in range(len(board_as_line)):
        #    print(str(i+1) + '|' + str(board_as_line[i]))
        visited_steps = set()
        steps_queue = deque()
        steps_queue.append((1, 0))
        visited_steps.add(1)
        while steps_queue:
            position, step = steps_queue.popleft()
            print(position, step)
            if position == l*l:
                return step
            for i in range(1, 7):
                if position + i <= l*l:
                    next_position = position + i
                    if board_as_line[position + i - 1] != -1:
                        next_position = board_as_line[position + i - 1]
                    if next_position not in visited_steps:
                        visited_steps.add(next_position)
                        steps_queue.append((next_position, step + 1))
        return -1

        
        # old dynamic programming solution. Does not work
        '''@cache
        def dp(position, step):
            if position in visited_steps:
                return float('inf') # we heet infinite loop
            if position > l*l:
                return float('inf')
            elif l*l == position:
                return 0
            if l*l - position <=6:
                return 1
            roll_results = [float('inf')]
            for i in range(1, 7, 1):
                if position + i - 1 < l*l:
                    if board_as_line[position + i - 1] != -1:
                        roll_results.append(dp(board_as_line[position + i - 1]) + 1, step + 1)
                    else:
                        roll_results.append(dp(position + i) + 1, step + 1)
            res = min(roll_results)
            visited_steps[position] = res
            return res
        
        res =  dp(1, 0)
        #print(visited_steps)
        if res == float('inf'):
            res = -1
        return res'''

        
board = [[-1,116,130,-1,-1,88,-1,-1,64,87,-1,-1,-1],
         [-1,-1,-1,124,-1,-1,-1,-1,-1,30,-1,-1,-1],
         [-1,-1,124,70,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,16,-1,71,-1,-1,-1,89,-1,-1,-1,-1],
         [-1,-1,134,-1,-1,51,-1,-1,-1,-1,-1,125,-1],
         [-1,-1,-1,-1,88,-1,-1,-1,-1,-1,163,27,-1],
         [-1,-1,127,-1,-1,95,129,-1,-1,-1,-1,-1,9],
         [-1,-1,144,-1,-1,-1,-1,-1,52,-1,-1,-1,-1],
         [-1,-1,128,-1,-1,-1,-1,-1,31,-1,-1,-1,-1],
         [64,-1,-1,149,38,-1,-1,143,-1,84,-1,-1,-1],
         [-1,-1,-1,-1,121,-1,4,154,-1,96,14,-1,126],
         [-1,39,-1,52,-1,66,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,113,-1,37,-1,-1,117,-1,-1,-1]]
obj = Solution()
print(obj.snakesAndLadders(board))
