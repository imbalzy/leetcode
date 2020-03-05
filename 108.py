# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int],left=0,right=1000000000) -> TreeNode:
        if not nums:
            return None
        if right==1000000000:
            right=len(nums)-1
        k=(left+right+1)//2
        node=TreeNode(nums[k])
        if k!=left:
            node.left=self.sortedArrayToBST(nums,left,k-1)
        if k!=right:
            node.right=self.sortedArrayToBST(nums,k+1,right)
        return node
