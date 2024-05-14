#BOJ4963 섬의 개수 ( bfs )

import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

def isvalidate(x,y) :
  if x>=0 and y>=0 and x < w and y < h : return True
  else : False

def bfs(q) :
  while q:
    pos = q.popleft()
    x = pos[0]
    y = pos[1]
  
    for i in range(8) :
      nx = x + dx[i]
      ny = y + dy[i]
      if not isvalidate(nx,ny) : continue
      if graph[ny][nx] == 1 and not visited[ny][nx] :
        visited[ny][nx] = True
        q.append((nx,ny))

while True :
  w,h = map(int,input().split())
  if w == 0 and h == 0 : break
  graph = [list(map(int,input().split())) for _ in range(h)]
  visited = [ [False]*w for _ in range(h)]
  
  ans = 0
  for i in range(h) :
    for j in range(w) :
      if graph[i][j] == 1 and not visited[i][j] :
        visited[i][j] = True
        q = deque()
        q.append((j,i))
        bfs(q)
        ans += 1
  
  print(ans)
    
    

    

    
  
  

