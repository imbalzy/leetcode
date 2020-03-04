class Solution:
    def find(self,board, x,y,n)-> bool:
        if n==len(self.word):
            return True
        if x>0:
            x1=x-1
            y1=y
            t=board[x1][y1]
            board[x1][y1]='*'
            if t==self.word[n]:
                if self.find(board,x1,y1,n+1):
                    return True
            board[x1][y1]=t
        if x<len(board)-1:
            x1=x+1
            y1=y
            t=board[x1][y1]
            board[x1][y1]='*'
            if t==self.word[n]:
                if self.find(board,x1,y1,n+1):
                    return True
            board[x1][y1]=t
        if y>0:
            x1=x
            y1=y-1
            t=board[x1][y1]
            board[x1][y1]='*'
            if t==self.word[n]:
                if self.find(board,x1,y1,n+1):
                    return True
            board[x1][y1]=t
        if y<len(board[0])-1:
            x1=x
            y1=y+1
            t=board[x1][y1]
            board[x1][y1]='*'
            if t==self.word[n]:
                if self.find(board,x1,y1,n+1):
                    return True
            board[x1][y1]=t
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word=word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    t=board[i][j]
                    board[i][j]='*'
                    if self.find(board,i,j,1):
                        return True
                    board[i][j]=t
        return False
    
