# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        n=[root]
        result=[]
        b=False
        while n:
            last=n
            n=[]
            t=[]
            b=not b

            for i in range(len(last)):

                r=last[len(last)-1-i]
                t.append(r.val)
                if b:
                    if r.left:
                        n.append(r.left)
                    if r.right:
                        n.append(r.right)
                else:
                    if r.right:
                        n.append(r.right)
                    if r.left:
                        n.append(r.left)
            result.append(t)
        return result
