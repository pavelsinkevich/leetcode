'''Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 '''
 # Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #res = []
        #res.append([])
        #l = len(nums)
        #res[0].append((l//2, nums[l//2]))

        def subArrayToBST(subarray, parent, is_left):
            l = len(subarray)
            if l != 0:
                tn = TreeNode(subarray[l//2])
                if parent:
                    if is_left == 1:
                        parent.left = tn
                    else:
                        parent.right = tn
                if l > 1:
                    subArrayToBST(subarray[:l//2], tn, 1)
                    subArrayToBST(subarray[l//2 + 1:], tn, 0)
                return tn
        root = subArrayToBST(nums, None, 0)

        return root

nums = [-10,-3,0,5,9]
obj = Solution()
root = obj.sortedArrayToBST(nums)
res = []
res.append(root.val)
def flattenTree(tn):
    if tn:
        if tn.left or tn.right:
            if tn.left:
                res.append(tn.left.val)
            else:
                res.append(None)
            if tn.right:
                res.append(tn.right.val)
            else:
                res.append(None)
            flattenTree(tn.left)
            flattenTree(tn.right)
flattenTree(root)
if res[-1] == None:
    del res[-1]
print(res)