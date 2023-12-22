'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 '''
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_len = 0
    
    def processNode(self, node, current_depth):
        if node.left:
            self.processNode(node.left, current_depth + 1)
        if node.right:
            self.processNode(node.right, current_depth + 1)
        if not node.left and not node.right:
            self.max_len = max(self.max_len, current_depth)
            
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.processNode(root, 1)
        return self.max_len
