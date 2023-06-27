
#BOJ14500 테트로미노
import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n) ]
visited = [[False for _ in range(m)] for _ in range(n)] 

max_value = max(map(max,board)) #최대값

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0 #결과

#유효성검사
def isvalidate(x,y) :
  if x >= 0 and y >= 0 and x < m and y < n : return True
  else : return False

#DFS
def dfs(x,y,current,length) :
  global ans
  if ans > current + max_value*(4-length) : return # 가지치기(백트래킹)
  if length == 4 : #블록이 4개인 경우
    ans = max(ans,current)
    return 
    
  for i in range(4) :
    nx = x + dx[i] 
    ny = y + dy[i] 
    if isvalidate(nx,ny) and not visited[ny][nx] :
        if length == 2 : # 'ㅗ' 모형이 가능하도록 뒤로이동
          visited[ny][nx] = True
          dfs(x,y,current+board[ny][nx],length+1)
          visited[ny][nx] = False
        visited[ny][nx] = True
        dfs(nx,ny,current+board[ny][nx],length+1)
        visited[ny][nx] = False

#문제풀이
for i in range(n) :
  for j in range(m) :
    visited[i][j] = True
    dfs(j,i,board[i][j],1)
    visited[i][j] = False
    
print(ans)
    