'''Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points 
such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.'''
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        x_coordinates =list(list(zip(*points))[0])
        x_coordinates.sort()
        minDist = 0
        for i in range(1, len(x_coordinates)):
            minDist = max(minDist, x_coordinates[i] - x_coordinates[i-1])
        return minDist

points = [[8,7],[9,9],[7,4],[9,7]]
obj = Solution()
print(obj.maxWidthOfVerticalArea(points))