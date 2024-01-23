'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dp(current_stair):
            res = 0
            if current_stair < n:
                res += dp(current_stair + 1)
            if current_stair + 1 < n:
                res += dp(current_stair + 2) + 1
            return res

        return dp(0) + 1

obj = Solution()
n = 3
print(obj.climbStairs(n))
