class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals==[]:
            return []
        a=[]
        intervals=sorted(intervals,key=operator.itemgetter(0))
        left=intervals[0][0]
        right=intervals[0][1]
        for i in range(1,len(intervals)):
            n=intervals[i]
            if n[0]<=right:
                right=max(right,n[1])
            else:
                a.append([left,right])
                left=n[0]
                right=n[1]
        a.append([left,right])
        return a
