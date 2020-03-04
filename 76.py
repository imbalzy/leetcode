class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=='':
            return ''
        dic=[0]*58
        for c in t:
            dic[ord(c)-65]+=1
        i=0
        j=-1
        l=[0]*58
        count=len(t)
        while count>0 and j<len(s)-1:
            j+=1
            l[ord(s[j])-65]+=1
            b=True
            if l[ord(s[j])-65]<=dic[ord(s[j])-65]:
                count-=1
        if j==len(s)-1 and count>0:
            return ''
        m=j-i+1
        r=s[i:j+1]
        while j<len(s) and i<len(s):
            l[ord(s[i])-65]-=1
            while dic[ord(s[i])-65]>l[ord(s[i])-65] and j<len(s)-1:
                j+=1
                l[ord(s[j])-65]+=1
            if dic[ord(s[i])-65]>l[ord(s[i])-65]:
                break
            i+=1
            if j-i+1<m:
                m=j-i+1
                r=s[i:j+1]
        return r
        
