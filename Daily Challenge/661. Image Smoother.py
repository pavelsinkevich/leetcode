'''An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell 
and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells 
of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
'''
from collections import defaultdict
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(img)
        m = len(img[0])
        cell_neighbors = defaultdict(list)
        for i in range(n):
            for j in range(m):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        cell_neighbors[(i+dx,j+dy)].append(img[i][j])
        for i in range(n):
            for j in range(m):
                img[i][j] = sum(cell_neighbors[(i, j)]) // len(cell_neighbors[(i, j)])

        return img
        
img = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
print(obj.imageSmoother(img))
