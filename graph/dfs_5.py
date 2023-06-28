#BOJ2667 단지번호 붙이기

import sys
input= sys.stdin.readline

n = int(input())
board = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
visited = [ [False]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = []

def isvalidate(x,y):
  if x >= 0 and y >= 0 and x < n and y < n : return True
  else : return False
    
def dfs(x,y,board) :
  global total
  if board[y][x] == 0 : return
  else : total += 1

  for i in range(4) :
    nx = x + dx[i] 
    ny = y + dy[i] 
    if isvalidate(nx,ny) and not visited[ny][nx] :
      visited[ny][nx] = True
      dfs(nx,ny,board)

for i in range(n) :
  for j in range(n) :
    if board[i][j] == 1 and not visited[i][j] :
      visited[i][j] = True
      total = 0
      dfs(j,i,board)
      ans.append(total)


ans.sort()
print(len(ans))
print(*ans,sep="\n")
      
        
    
  
  