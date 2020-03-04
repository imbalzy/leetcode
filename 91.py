class Solution:
    def numDecodings(self, s: str) -> int:
        n=1
        a=[0]*(len(s)+2)
        a[-1]=1
        for i in range(0,len(s)):
            if s[i]!='0':
                a[i]+=a[i-1]
                if i!=len(s)-1 and (s[i]=='1' or (s[i]=='2' and ord(s[i+1])<=ord('6'))):
                    a[i+1]+=a[i-1]
        return a[len(s)-1]
