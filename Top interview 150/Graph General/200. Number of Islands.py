'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges 
of the grid are all surrounded by water.'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        land_sections = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    land_sections[(i, j)] = 0
        

        def draw_island(land_section, current_island):
            if land_section in land_sections:
                if land_sections[land_section] == 0:
                    land_sections[land_section] = current_island
                    up = (land_section[0], land_section[1] - 1)
                    draw_island(up, current_island)
                    down = (land_section[0], land_section[1] + 1)
                    draw_island(down, current_island)
                    left = (land_section[0] - 1, land_section[1])
                    draw_island(left, current_island)
                    right = (land_section[0] + 1, land_section[1])
                    draw_island(right, current_island)
        
        current_island = 0
        for land_section in land_sections:
            if land_sections[land_section] == 0:
                current_island +=1
                draw_island(land_section, current_island)

        return current_island

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
print(obj.numIslands(grid))