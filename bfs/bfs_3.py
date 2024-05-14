from collections import deque

n,m,start = map(int,input().split())
edges = [[] for _ in range(n+1)]

# 간선 초기화
for _ in range(m) :
  a,b = map(int,input().split())
  edges[a].append(b)
  edges[b].append(a)

# 인접노드 오름차순 정렬
for i in range(n+1) :
  edges[i].sort()

# DFS
def dfs(edges,v,visited) :
  print(v,end=" ")
  visited[v] = True
  for next in edges[v] :
    if not visited[next] : dfs(edges,next,visited)

#BFS
def bfs(edges,v,visited) :
  q = deque([v])
  visited[v] = True
  while q  :
    node = q.popleft()
    print(node,end=" ")
    for next in edges[node] :
      if not visited[next] :  
        visited[next] = True 
        q.append(next)

# 수행
visited = [False] * (n+1) #방문이력테이블
dfs(edges,start,visited) 
print()
visited = [False] * (n+1) #방문이력테이블 원복
bfs(edges,start,visited)

  