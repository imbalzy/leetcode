class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        a=[board]
        b=[0]
        s=set()
        while a!=[]:
            x=a.pop(0)
            index=b.pop(0)
            if x==[[1,2,3],[4,5,0]]:
                return index
            for i in range(2):
                for j in range(3):
                    if x[i][j]==0:
                        break
                if x[i][j]==0:
                    break
            if i!=0:
                t=[row[:] for row in x]
                t[i][j]=t[i-1][j]
                t[i-1][j]=0
                tu=tuple(t[0]+t[1])
                if not (tu in s):
                    s.add(tu)
                    a.append(t)
                    b.append(index+1)
            else:
                t=[row[:] for row in x]
                t[i][j]=t[i+1][j]
                t[i+1][j]=0
                tu=tuple(t[0]+t[1])
                if not (tu in s):
                    s.add(tu)
                    a.append(t)
                    b.append(index+1)
            if j!=0:
                t=[row[:] for row in x]
                t[i][j]=t[i][j-1]
                t[i][j-1]=0
                tu=tuple(t[0]+t[1])
                if not (tu in s):
                    s.add(tu)
                    a.append(t)
                    b.append(index+1)
            if j!=2:
                t=[row[:] for row in x]
                t[i][j]=t[i][j+1]
                t[i][j+1]=0
                tu=tuple(t[0]+t[1])
                if not (tu in s):
                    s.add(tu)
                    a.append(t)
                    b.append(index+1)
        return -1
