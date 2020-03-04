class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        while nums[j]==2 and j>0:
            j-=1
        while nums[i]==0 and i<len(nums)-1:
            i+=1
        if i==len(nums)-1 or j==0:
            return
        k=i
        while k<=j:
            if k<i:
                k+=1
            elif nums[k]==0:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1
                while nums[i]==0:
                    i+=1
            elif nums[k]==2:
                nums[k],nums[j]=nums[j],nums[k]
                j-=1
                while nums[j]==2:
                    j-=1
            else:
                k+=1
