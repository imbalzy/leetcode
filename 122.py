class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        s=0
        b=-1
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i+1]<=prices[i]:
                i+=1
            b=prices[i]
            while i<len(prices)-1 and prices[i+1]>prices[i]:
                i+=1
            s+=prices[i]-b
            b=-1
        if b>=0:
            s+=prices[i]-b
        return s
