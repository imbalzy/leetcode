class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(1)
        nums.append(1)
        dp=[[0 for i in range(len(nums)+2)] for i in range(len(nums)+2)]
        for i in range(n):
            dp[i][i]=nums[i]*nums[i+1]*nums[i-1]
        for i in range(1,n):
            for j in range(0,n-i):
                for k in range(0,i+1):
                    dp[j][j+i]=max(dp[j][j+i],dp[j][j+k-1]+dp[j+k+1][j+i]+nums[j-1]*nums[j+k]*nums[j+i+1])
        return dp[0][n-1]
