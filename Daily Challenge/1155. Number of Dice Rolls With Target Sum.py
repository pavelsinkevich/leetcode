'''You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, 
so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10 ** 9 + 7.'''
class Solution:
    def numRollsToTarget(self, dice_qty, faces_qty, target):
        def rollsToSubTarget(h, dice_qty, target):
            # if target is too small or if it is out of range
            if target <= 0 or target > (dice_qty * faces_qty):
                return 0
            if dice_qty == 1:
                return 1        # no need to check if target is within reach; already done before
            if (dice_qty, target) in h:
                return h[(dice_qty, target)]        # directly access from hash table
            res = 0
            for i in range(1, faces_qty + 1):
                res += rollsToSubTarget(h, dice_qty - 1, target - i)       # check all possible combinations
            h[(dice_qty, target)] = res
            return h[(dice_qty, target)]
        
        h = dict()
        return rollsToSubTarget(h, dice_qty, target) % (10 ** 9 + 7)

n = 2
k = 6
target = 7
obj = Solution()
print(obj.numRollsToTarget(n, k, target))