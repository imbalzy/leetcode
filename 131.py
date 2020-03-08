class Solution:
    # DP
    def partition(self, s: str) -> List[List[str]]:
        a=[[s[i]] for i in range(len(s))]
        for i in range(len(s)):
            if i!=len(s)-1:
                k=1
                while i-k>=0 and i+k<len(s) and s[i-k]==s[i+k]:
                    a[i-k].append(s[i-k:i+k+1])
                    k+=1
                if s[i]==s[i+1]:
                    a[i].append(s[i:i+2])
                    k=1
                    while i-k>=0 and i+k+1<len(s) and s[i-k]==s[i+k+1]:
                        a[i-k].append(s[i-k:i+k+2])
                        k+=1
        b=[[] for i in range(len(s)+1)]
        for n in a[0]:
            b[len(n)].append([n])
        for i in range(1,len(s)):
            for n in a[i]:
                for j in range(len(b[i])):
                    b[i+len(n)].append(b[i][j]+[n])
        return b[len(s)]
