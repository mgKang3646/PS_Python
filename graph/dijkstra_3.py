import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n,m,start = map(int,input().split())
d = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
  a,b,cost= map(int,input().split())
  graph[a].append((b,cost))

q = []
d[start] = 0
heapq.heappush(q,(0,start))

count = -1
max_cost = -1

while q :
  cost,now = heapq.heappop(q)
  if d[now] < cost : continue

  count += 1
  max_cost = max(max_cost,cost)

  for next in graph[now] :
    next_cost = next[1] + cost
    d[next[0]] = next_cost
    heapq.heappush(q,(next_cost,next[0]))


print(count,max_cost,end=" ")






  
