#BOJ2178 미로탐색

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
miro = [ list(map(int,input().rstrip("\n"))) for _ in range(n) ]
miro_cost = [ [100001]*m for _ in range(n) ]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isvalidate(x,y) :
  return True if x >= 0 and y >=0 and x < m and y < n else False
  
def dfs(x,y,cost) :
  if x == m-1 and y == n-1 : return
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i] 
    ncost= cost+1

    if isvalidate(nx,ny) and miro[ny][nx] == 1 :
      if miro_cost[ny][nx] > ncost : 
        miro_cost[ny][nx] = ncost
        dfs(nx,ny,ncost)

miro_cost[0][0] = 1
dfs(0,0,1)
print(miro_cost[n-1][m-1])
      
