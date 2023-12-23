'''Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. 
Return false otherwise.'''

class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = 0, 0
        visited = set()
        visited.add((x, y))
        for char in path:
            if char == 'N':
                    y += 1
            elif char == 'E':
                    x += 1
            elif char == 'W':
                    x -= 1
            elif char == 'S':
                    y -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False

        
path = "NES"
obj = Solution()
print(obj.isPathCrossing(path))