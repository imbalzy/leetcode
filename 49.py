class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table={}
        """
        result=[]
        table=[]
        for i in strs:
            b=True
            temp=[0]*26
            for c in i:
                temp[ord(c)-97]+=1
            for j in range(len(result)):
                if temp==table[j]:
                    result[j].append(i)
                    b=False
                    break
            if b:
                result.append([i])
                table.append(temp)
        """
        
        for i in range(len(strs)):
#            temp=[0]*26
#            for c in strs[i]:
#                temp[ord(c)-97]+=1
#            temp=tuple(temp)
            temp=tuple(sorted(strs[i]))
            if temp in table:
                table[temp].append(strs[i])
            else:
                table[temp]=[strs[i]]
        return table.values()
