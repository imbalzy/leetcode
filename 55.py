class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        n=0
        if nums==[0]:
            return True
        while i<=n and i<len(nums):
            if i+nums[i]>n:
                n=i+nums[i]
            i+=1
        if n>=len(nums)-1:
            return True
        return False 
