class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        m=len(matrix)
        n=len(matrix[0])
        result=[matrix[0][0]]
        x=0
        y=0
        dx=0
        dy=1
        xmax=m-1
        xmin=0
        ymax=n-1
        ymin=0
        t=0
        while t!=m*n-1:
            if y+dy>ymax:
                xmin+=1
                dx=1
                dy=0
            elif x+dx>xmax:
                dx=0
                dy=-1
                ymax-=1
            elif y+dy<ymin:
                xmax-=1
                dx=-1
                dy=0
            elif x+dx<xmin:
                dx=0
                dy=1
                ymin+=1
            else:
                x+=dx
                y+=dy
                result.append(matrix[x][y])
                t+=1
        return result
                    
            