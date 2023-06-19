
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,x,visited) :
  visited[x] = True

  for next in graph[x] :
    if not visited[next] :
      dfs(graph,next,visited)

count = 0
for i in range(1,n+1) :
  if not visited[i] : 
    dfs(graph,i,visited)
    count += 1

print(count)
  
  

  