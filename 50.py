class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        sign=True if n>=0 else False
        n=abs(n)
        l=[]
        a=1.0
        while n!=0:
            l=[n%2]+l
            n=n//2
        for i in l:
            if i!=0:
                a=a*a*x
            else:
                a=a*a
        return a if sign else 1.0/a
