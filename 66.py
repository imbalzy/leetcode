class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        digits[n-1]+=1
        i=n-1
        while i>=1 and digits[i]==10:
            digits[i]=0
            i-=1
            digits[i]+=1
        if i==0 and digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return(digits)
