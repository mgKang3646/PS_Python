maxY, maxX = map(int,input().split())
 # 얼음틀
graph = []
for i in range(maxY) :
  graph.append(list(map(int,input())))

# 방문여부 자료구조
visited = [] 
for i in range(maxX) :
  visited.append([False] * maxY )

#상하좌우 이동 자료구조
dx = [ 0, 0, -1 , 1 ]
dy = [ 1, -1, 0 , 0 ]


# 좌표 검증 함수
def validateIndex(x,y) :
  if x < 0 or x >= maxX or y < 0 or y >= maxY :
      return False
  else : return True 

# DFS 알고리즘 구현 함수 
def dfs(x, y) :
  visited[x][y] = True # 방문처리
  if not validateIndex(x,y) :
    return # 정확한 값을 리턴해야 함수를 사용하는 쪽이 편하다.
  if graph[x][y] == 1 :
    return # 정확한 값을 리턴해야 함수를 사용하는 쪽이 편하다.

  #상하좌우를 for문으로 구현, 
  for i in range(4) :
    tmpX = x+dx[i] #이동 할 x 좌표
    tmpY = y+dy[i] #이동 할 y 좌표

    #좌표 유효성 검사 
    if not validateIndex(tmpX,tmpY) :
      print("부적격 인덱스 : ",tmpX," ",tmpY)
      continue 
    #좌표 방문여부 검사
    if visited[tmpX][tmpY] :
      print("True 이다!",tmpX," ",tmpY)
      continue
    # 조건검사 통과시 함수 수행
    dfs(tmpX,tmpY)

count = 0
for j in range(maxY) :
  for i in range(maxX) :
      #이미 방문한 곳은 재방문X
      if visited[i][j] :
        continue
      dfs(i,j)
      count += 1

print("결과 : ", count)
