
#BOJ14500 테트로미노
import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n) ]
visited = [[False for _ in range(m)] for _ in range(n)] 

max_value = max(map(max,board))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = [
  [(1,0),(-1,0),(0,-1)],
  [(1,0),(-1,0),(0,1)],
  [(0,1),(0,-1),(1,0)],
  [(0,1),(0,-1),(-1,0)]
]

ans = 0

#유효성검사
def isvalidate(x,y) :
  if x >= 0 and y >= 0 and x < m and y < n : return True
  else : return False

#DFS
def dfs(x,y,total,lengh) :
  global ans

  if ans > total + max_value*(4-lengh) : return
  if lengh == 4 : #길이가 4인 경우
    ans = max(ans,total)
    return 
    
  for i in range(4) :
    nx = x + dx[i] 
    ny = y + dy[i] 
    if isvalidate(nx,ny) and not visited[ny][nx] :
        visited[ny][nx] = True
        dfs(nx,ny,total+board[ny][nx],lengh+1)
        visited[ny][nx] = False

# 'ㅗ' 모양
def tshape(x,y) :
  total = 0
  for i in range(4) :
    tmp = board[y][x]
    flag = True
    for j in range(3) :
      position = t[i][j] 
      tx = position[0]
      ty = position[1]
      nx = x + tx
      ny = y + ty
      if isvalidate(nx,ny) :
        tmp += board[ny][nx]
      else : flag = False

    total = ( max(total,tmp) if flag else total )
  return total

#문제풀이
for i in range(n) :
  for j in range(m) :
    visited[i][j] = True
    dfs(j,i,board[i][j],1)
    visited[i][j] = False
    ans = max(ans,tshape(j,i))
    
print(ans)
    