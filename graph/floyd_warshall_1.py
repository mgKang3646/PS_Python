
INF = int(1e9) #무한

n = int(input()) #노드의 수
m = int(input()) #간선의 수

#2차원 테이블 만들기
graph = [[INF]*(n+1) for _ in range(n+1)]

#출발점과 도착점이 동일한 경우 0으로 초기화
for x in range(1,n+1) :
  for y in range(1,n+1) :
    if x == y :
      graph[x][y] = 0

#간선정보 초기화하기
for _ in range(m) :
  start,end,value = map(int,input().split())
  graph[start][end] = value

#플로이드-워셜 알고리즘 구현 ( 3중 for문  )
for middle in range(1,n+1) : # 경유점
  for start in range(1,n+1) : # 시작점
    for end in range(1,n+1) : # 도착점
      current = graph[start][end] # 현재 최단경로
      value = graph[start][middle] + graph[middle][end] # 경유시 최단경로
      graph[start][end] = min(current,value) # 최단경로 초기화

#출력
for start in range(1,n+1) :
  for end in range(1,n+1) :
    if graph[start][end] == INF : print("INFINITY")
    else : print(graph[start][end],end=" ")
  print()
      