

#BOJ1707 이분그래프
from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
R,B = 1,-1 # 서로 다른 집합의 색상정보 ( R : RED, B : BLUE )

#넓이 우선 탐색 ( BFS )
def bfs(bipartite,i) :
  global flag 
  bipartite[i] = R # RED로 칠하기 
  q =deque([i])
  while q :
    i = q.popleft() #탐색노드 가져오기
    for node in graph[i] : # 인접노드 가져오기 
      if bipartite[node] != 0 : #방문된 노드라면 색상비교하기
        if bipartite[node] == bipartite[i] : #색상이 일치하면 이분 그래프X
          flag = False
          return #함수종료
      else : #방문된적 없다면 반대 색상으로 색칠하기
        bipartite[node] = -bipartite[i] 
        q.append(node) # 큐에 넣기 

#그래프 탐색시작 
for _ in range(k) :
  v,e = map(int,input().split())  # 간선정보 가져오기
  bipartite = [0] * (v+1) # 색상 테이블 
  graph = [[] for _ in range(v+1)] # 그래프

  #그래프 초기화
  for i in range(e) :
    a,b = map(int,input().split())
    graph[a].append(b) # 양방향 그래프
    graph[b].append(a)

  #BFS로 이분그래프 색칠하기
  flag = True
  for i in range(1,v+1) :
    if not flag : break
    if bipartite[i] == 0 : bfs(bipartite,i)

  #출력
  print("YES" if flag else "NO")

      

  
    
      

    
    




  



