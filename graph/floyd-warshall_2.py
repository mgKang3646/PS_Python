
INF = int(1e9)
n,m = map(int, input().split())

graph = [ [INF]*(n+1) for _ in range(n+1)]

#그래프 간선 초기화
for _ in range(m) :
  com1, com2 = map(int,input().split())
  graph[com1][com2] = 1 #양방향 간선 
  graph[com2][com1] = 1 #양방향 간선 

x,k = map(int,input().split())


#D(1,K) 최단경로 + D(K,X) 최단경로 
for middle in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1,n+1) :
      graph[start][end] = min(graph[start][end], graph[start][middle]+graph[middle][end])

result = graph[1][k] + graph[k][x] #D(1,K) 최단경로 + D(K,X) 최단경로 

#출력
if result >= INF : print(-1)
else : print(result)