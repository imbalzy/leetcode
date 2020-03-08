class Solution:
    # Would be more efficient to edit directly on the original board
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        x=len(board)
        y=len(board[0])
        visit=[[False if board[i][j]=='X' else True for j in range(y)] for i in range(x)]
        for i in range(x):
            for j in range(y):
                if visit[i][j] and board[i][j]=='O':
                    queue=[[i,j]]
                    visit[i][j]=False
                    k=0
                    surround=True
                    while len(queue)>k:
                        if queue[k][0]==0 or queue[k][0]==x-1 or queue[k][1]==y-1 or queue[k][1]==0:
                            surround=False
                        if queue[k][1]!=y-1 and visit[queue[k][0]][queue[k][1]+1]:
                            queue.append([queue[k][0],queue[k][1]+1])
                            visit[queue[k][0]][queue[k][1]+1]=False
                        if queue[k][1]!=0 and visit[queue[k][0]][queue[k][1]-1]:
                            queue.append([queue[k][0],queue[k][1]-1])
                            visit[queue[k][0]][queue[k][1]-1]=False
                        if queue[k][0]!=x-1 and visit[queue[k][0]+1][queue[k][1]]:
                            queue.append([queue[k][0]+1,queue[k][1]])
                            visit[queue[k][0]+1][queue[k][1]]=False
                        if queue[k][0]!=0 and visit[queue[k][0]-1][queue[k][1]]:
                            queue.append([queue[k][0]-1,queue[k][1]])
                            visit[queue[k][0]-1][queue[k][1]]=False
                        k+=1
                    if surround:
                        for i1,j1 in queue:
                            board[i1][j1]='X'
        return
        
