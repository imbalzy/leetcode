class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        if numRows==0:
            return []
        result.append([1])
        for i in range(1,numRows):
            t=[1]
            for j in range(i-1):
                t.append(result[i-1][j]+result[i-1][j+1])
            t.append(1)
            result.append(t)
        return result
