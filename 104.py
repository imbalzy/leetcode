# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        n=[root]
        j=0
        while n:
            j+=1
            last=n
            n=[]
            for i in range(len(last)):
                r=last[len(last)-1-i]
                if r.left:
                    n.append(r.left)
                if r.right:
                    n.append(r.right)
        return j
