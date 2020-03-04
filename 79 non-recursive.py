class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        a=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    a.append([[i,j]])
        while a!=[]:
            n=a.pop()
            if len(n)==len(word):
                return True
            x=n[len(n)-1][0]
            y=n[len(n)-1][1]
            if x>0:
                x1=x-1
                y1=y
                if board[x1][y1]==word[len(n)]:
                    if not [x1,y1] in n:
                        a.append(n+[[x1,y1]])
            if x<len(board)-1:
                x1=x+1
                y1=y
                if board[x1][y1]==word[len(n)]:
                    if not [x1,y1] in n:
                        a.append(n+[[x1,y1]])
            if y>0:
                x1=x
                y1=y-1
                if board[x1][y1]==word[len(n)]:
                    if not [x1,y1] in n:
                        a.append(n+[[x1,y1]])
            if y<len(board[0])-1:
                x1=x
                y1=y+1
                if board[x1][y1]==word[len(n)]:
                    if not [x1,y1] in n:
                        a.append(n+[[x1,y1]])
        return False
