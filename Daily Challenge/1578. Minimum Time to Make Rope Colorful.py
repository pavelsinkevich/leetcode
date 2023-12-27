'''Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. 
Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] 
is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.'''
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        min_cost = 0
        colors_list = [x for x in colors]
        i = 0
        while i< len(colors_list) - 1:
            if colors_list[i] == colors_list[i+1]:
                if neededTime[i] < neededTime[i+1]:
                    min_cost += neededTime[i]
                    del colors_list[i]
                    del neededTime[i]
                else:
                    min_cost += neededTime[i+1]
                    del colors_list[i+1]
                    del neededTime[i+1]
            else:
                i += 1
        return min_cost


colors = "abaac"
neededTime = [1,2,3,4,5]
obj = Solution()
print(obj.minCost(colors, neededTime))