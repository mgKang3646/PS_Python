import heapq #힙큐 라이브러리 추가
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [ [] for i in range(n+1)] # 그래프
distance = [ INF ] * (n+1) # 최단경로 테이블

#그래프 간선 초기화
for _ in range(m) :
  node,target,cost = map(int, input().split())
  graph[node].append((target,cost))

#다익스트라 함수
def dijkstra(start) :
  q = [] # 큐가 사용할 공간
  heapq.heappush(q,(0,start))  # Start 데이터 push
  distance[start] = 0 # 최단경로테이블 최적해 갱신

  while q : # 큐가 비어질때까지 반복
    cost,node = heapq.heappop(q) #우선순위가 높은 데이터 POP ( 비용, 현재노드 )
    
    # 이미 방문한 노드인 경우 
    if distance[node] < cost : continue 

    for next in graph[node] :
      next_cost = next[1] + cost
      if next_cost < distance[next[0]] : 
        distance[next[0]] = next_cost #최단경로 테이블 최적해로 갱신
        heapq.heappush(q,(next_cost,next[0])) # 데이터 우선순위큐에 PUSH

#다익스트라 알고리즘 함수 호출
dijkstra(start)

#출력
for i in range(1,n+1) :
  if distance[i] == INF : print("INFINITY")
  else : print(distance[i])
  