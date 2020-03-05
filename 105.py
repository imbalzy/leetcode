# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Hashed
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        h={}
        for i in range(len(inorder)):
            h[inorder[i]]=i
        if not preorder:
            return None
        def recur(preleft,inleft,length):
            node=TreeNode(preorder[preleft])
            i=h[preorder[preleft]]
            llength=i-inleft
            if i!=inleft:
                node.left=recur(preleft+1,inleft,llength)
            if i!=inleft+length-1:
                node.right=recur(preleft+1+llength,inleft+1+llength,length-llength-1)
            return node
        return recur(0, 0, len(preorder))
