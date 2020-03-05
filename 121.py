class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low=prices[0]
        high=prices[0]
        m=0
        for i in range(1,len(prices)):
            if low>prices[i]:
                low=prices[i]
                high=prices[i]
            elif high<prices[i]:
                high=prices[i]
                m=max(m,high-low)
        return m
