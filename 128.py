class Solution:
    # myshit
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d={}
        for n in nums:
            d[n]=1
        visited=set()
        def recur(n):
            if not n in visited:
                visited.add(n)
                if n-1 in d:
                    d[n]=recur(n-1)+1
                if n+1 in d:
                    recur(n+1)
            return d[n]
        m=0
        for n in nums: 
            m=max(m,recur(n))
        return m
    #same logic but using while instead of recursion(I am so dumb)
    def longestConsecutive0(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
