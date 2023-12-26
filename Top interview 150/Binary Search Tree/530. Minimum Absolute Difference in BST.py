'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values 
of any two different nodes in the tree.'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val_list = []
        def saveAllValues(node):
            if node:
                val_list.append(node.val)
                saveAllValues(node.left)
                saveAllValues(node.right)
        saveAllValues(root)
        val_list.sort()
        min_diff = float("inf")
        for i in range(len(val_list) - 1):
            min_diff = min(min_diff, abs(val_list[i] - val_list[i+1]))
        return min_diff
        
root = [4,2,6,1,3, None, None]
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
print(obj.getMinimumDifference(node_list[0]))        