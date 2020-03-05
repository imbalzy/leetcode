# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isequal(self,left,right):
        if left.val!=right.val:
            return False
        if (left.left==None)!=(right.right==None):
            return False
        if (left.right==None)!=(right.left==None):
            return False
        if left.left:
            if right.right:
                if not self.isequal (left.left,right.right):
                    return False
        if left.right:
            if right.left:
                if not self.isequal (left.right,right.left):
                    return False
        return True
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not(root.right or root.left):
            return True
        if root.right and root.left:
            return self.isequal (root.left,root.right)
        return False
