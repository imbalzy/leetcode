class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column=[1]*len(matrix[0])
        row=[1]*(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    column[j]=0
                    row[i]=0
        for i in range(len(matrix)):
            if row[i]==0:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        for j in range(len(matrix[0])):
            if column[j]==0:
                for i in range(len(matrix)):
                    matrix[i][j]=0
        return
