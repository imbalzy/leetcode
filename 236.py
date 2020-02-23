# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d=set()
        d.add(p)
        d.add(q)
        ancestor={}
        ancestor[root]=None
        r1=[root]
        while (not p in ancestor) or (not q in ancestor):
            r=r1
            r1=[]
            for n in r:
                if n.left!=None:
                    ancestor[n.left]=n
                    r1.append(n.left)
                if n.right!=None:
                    ancestor[n.right]=n
                    r1.append(n.right)
        while True:
            if p in ancestor and p!=None:
                p=ancestor[p]
                if p in d:
                    return p
                else:
                    d.add(p)
            if q in ancestor and q!=None:
                q=ancestor[q]
                if q in d:
                    return q
                else:
                    d.add(q)
        return
