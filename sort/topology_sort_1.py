from collections import deque

n,e = map(int,input().split())

#자료구조 
indegree = [0]*(n+1) #진입차수테이블
graph = [[] for i in range(n+1)] #그래프테이블 (노드 간 의존관계)

#그래프 간선 초기화
for _ in range(e) :
  a,b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1

#위상정렬 알고리즘
def topology_sort() : 
  q = deque() #큐생성
  result = [] #결과테이블
  
  #진입차수가 0인 노드 탐색
  for i in range(1,n+1) :
    if indegree[i] == 0 : q.append(i) #큐에 등록
  
  while q : #큐가 비어질때까지 반복
    now = q.popleft() #선입선출
    result.append(now) 
    # 의존관계 노드 가져오기
    for node in graph[now] :
      indegree[node] -= 1 #진입차수 제거
      #진입차수가 0이면 큐에 등록
      if indegree[node] == 0 : 
        q.append(node)
  #출력
  for value in result :
    print(value,end=" ")


topology_sort()

  

