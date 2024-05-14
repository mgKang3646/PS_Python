from collections import deque

n,m = map(int, input().split())  # n : 행, m : 열
 
graph = [] # 이차행렬 ( 미로 )
for _ in range(n) :
  graph.append(list(map(int,input()))) # 이차행렬초기화

visited = [[False]*m for _ in range(n)] # 방문이력테이블

dx = [0,0,-1,1] #수평이동 상하좌우
dy = [-1,1,0,0] #수직이동 상하좌우

# 미로 밖으로 벗어나는지 검증하기
def is_validate(x,y) : # x : 행, y : 열
  if x >= n or x < 0 or y >=m or y < 0 : return False
  else : return True
  
q=deque() # 큐생성
q.append((0,0)) # 시작점 
while q :
  pointX,pointY = q.popleft() # 노드 방문하기
  visited[pointX][pointY] = True # 방문체크 
    
  for i in range(4) : # 상,하,좌,우 이동 ( 경우 4가지 )
    nx = pointX + dx[i]
    ny = pointY + dy[i]
    if not is_validate(nx,ny) : continue # 미로 밖을 벗어나는 경우 제외하기
    if graph[nx][ny] == 0 : continue # 노드값이 0인 경우 제외하기
    if not visited[nx][ny] :  # 방문이력이 있는 노드인 경우 제외하기
      q.append((nx,ny)) # 방문이력 없다면 해당 노드에 최초로 도달한 최단경로임을 의미하므로 큐에 삽입
      graph[nx][ny] = graph[nx][ny] + graph[pointX][pointY] # 경로 비용 갱신하기

print(graph[n-1][m-1]) # 목표지점 비용 출력하기

    
      
