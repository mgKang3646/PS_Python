
import sys
input = sys.stdin.readline # 데이터 수가 많은 경우, 더 빠르게 동작하도록 도와주는 함수
INF = int(1e9) #무한

n,m = map(int,input().split()) # n = 노드의 수, m = 간선의 수
start = int(input()) # 시작 지점

graph = [ [] for i in range(n+1) ] # 그래프 자료구조
visited = [False]*(n+1) # 탐색이력 자료구조
distance = [INF]*(n+1) # 최단경로 자료구조

#그래프 자료구조 초기화
for _ in range(m) :
  node,target,value = map(int,input().split()) # target : 인접노드, value : 간선비용
  graph[node].append((target,value)) # 노드에 (인접노드,간선비용) 추가

#탐색이력 없고 최단경로가 최솟값이 노드 반환
def get_smallest_node() :
  minValue = INF
  minIndex = 0
  for i in range(1, n+1) : #탐색이력 없는 최단경로를 가진 노드 탐색
    if not visited[i] and  distance[i] < minValue :
      minValue = distance[i]
      minIndex = i
  return minIndex

#다익스트라 알고리즘
def djikstra(start) :
  #START 초기화
  visited[start] = True #탐색이력 TRUE
  distance[start] = 0 #출발지 최단거리 : 0

  for line in graph[start] : # 인접노드 정보 가져오기
    distance[line[0]] = line[1] # 최단경로 자료구조 초기화
  # 알고리즘 시작
  for i in range(n) : 
    index = get_smallest_node() # 탐색이력 없고 최단경로가 최솟값인 노드 생성
    visited[index] = True # 탐색이력 TRUE

    for line in graph[index] : # 인접노드 정보 가져오기
      cost = distance[index] + line[1] # 비용계산 
      if cost < distance[line[0]] :distance[line[0]] = cost # 최단경로 갱신
      #Greedy 반복

djikstra(start) #다익스트라 알고리즘 실행

# 출력
for i in range(1,n+1) :
  if distance[i] == INF : print("INFINITY")
  else : print(distance[i])



