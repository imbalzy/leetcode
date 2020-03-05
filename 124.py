# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.m=root.val
        self.root=root
        def recur(root: TreeNode):
            left=0
            right=0
            m=root.val
            if root.left:
                left=recur(root.left)
                if left>0:
                    m+=left
            if root.right:
                right=recur(root.right)
                if right>0:
                    m+=right
            self.m=max(self.m,m)
            if self.root==root:
                return max(root.val, root.val+max(left,right))
            else:
                return max(0, root.val, root.val+max(left,right))
        return max(recur(root),self.m)
