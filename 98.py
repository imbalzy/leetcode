# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#one line
class Solution:
    def isValidBST(self, root: TreeNode,l=float('-inf'), r=float('inf')) -> bool:
        return (root.val>l and root.val<r and (self.isValidBST(root.left,l,min(r,root.val)) if root.left else True) and (self.isValidBST(root.right,max(l,root.val),r) if root.right  else True))if root else True
