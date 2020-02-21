#binary insertion
#could use two heaps instead
class MedianFinder:
    def __init__(self):
        self.a=[]
        """
        initialize your data structure here.
        """
        

    def addNum(self, num: int) -> None:
        i=0
        j=len(self.a)-1
        while i<=j:
            m=(j+i)//2
            if self.a[m]>=num:
                j=m-1
            else:
                i=m+1
        self.a.insert(i,num)
                
    def findMedian(self) -> float:

        if len(self.a)&1==0:
            return self.a[len(self.a)//2]/2+self.a[len(self.a)//2-1]/2
        else:
            return self.a[len(self.a)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()