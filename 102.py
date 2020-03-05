# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        n=[root]
        result=[]
        while n:
            last=n
            n=[]
            t=[]
            for r in last:
                t.append(r.val)
                if r.left:
                    n.append(r.left)
                if r.right:
                    n.append(r.right)
            result.append(t)
        return result
