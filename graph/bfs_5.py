

#BOJ2178 미로탐색 
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
miro = [ list(map(int,input().rstrip("\n"))) for _ in range(n) ]
cost = [ [100001] *m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isvalidate(x,y) :
  return True if x>=0 and y>=0 and x<m and y<n else False

def bfs(q) :
  while q :
    qv = q.popleft()
    x,y,cost_now = qv[0],qv[1],qv[2]

    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      cost_next = cost_now+1

      if isvalidate(nx,ny) and miro[ny][nx] == 1 :
        if cost[ny][nx] > cost_next : 
          cost[ny][nx] = cost_next
          q.append((nx,ny,cost_next))

q = deque()
q.append((0,0,1))
bfs(q)
print(cost[n-1][m-1])

  
