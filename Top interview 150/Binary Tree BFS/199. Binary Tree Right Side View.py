'''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see 
ordered from top to bottom.'''
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.tree_items = defaultdict(list)
    def processNode(self, node, level):
        if node:
            self.tree_items[level].append(node.val)
            self.processNode(node.left, level+1)
            self.processNode(node.right, level+1)


    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.processNode(root, 0)
        right_side_view = []
        for i in range(len(self.tree_items)):
            right_side_view.append(self.tree_items[i][-1])
        return right_side_view


        
root = [1,2,3,None,5,None,4]
l = len(root)
node_list = [None for x in root]
for i in reversed(range(l)):
    left = None
    right = None
    if i*2+2 < l:
        left = node_list[i*2+1]
        right = node_list[i*2+2]
    if root[i]:
        node_list[i] = TreeNode(root[i], left, right)

obj = Solution()
print(obj.rightSideView(node_list[0]))

    