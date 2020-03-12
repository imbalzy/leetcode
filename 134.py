class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        balance=0
        k=0
        if sum(cost)>sum(gas):
            return -1
        for i in range(len(cost)):
            balance+=gas[i]-cost[i]
            if balance<0:
                k=i+1
                balance=0
        return k
