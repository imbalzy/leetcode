# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        result=[]
        while stack:
            k=stack[-1]
            if k.left:
                stack.append(k.left)
                k.left=None
            else:
                result.append(stack.pop().val)
                if k.right:
                    stack.append(k.right)
                    k.right=None
            #print(stack[-1].val)
        return result
