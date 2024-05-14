
from collections import deque

MAX = 1000000
n,k = map(int,input().split())
d = [0] * (MAX+1)

#BFS 함수
def bfs(start,target) :
  q = deque()
  q.append(start) # 첫 루트노트 PUSH

  while q :
    value = q.popleft() 
    if value == target : break
    else :
      for next in (value+1,value-1,value*2) : # 부모가 자식을 큐에 PUSH하기
        if 0 <= next <= MAX and not d[next] : # 유효값이 아니거나 방문된 노드이면 제외
          d[next] = d[value] + 1 # 연산횟수 테이블 초기화
          q.append(next) # 큐에 PUSH
      
  return d[value]
      

print(bfs(n,k))

  
    


      
