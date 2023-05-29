n,m = map(int,input().split())  # N X M
x,y,d = map(int,input().split()) # x,y : 현재좌표 , d : 현재방향

visited = [[False]*(n) for _ in range(m)] #방문여부 테이블
dx = [0,1,0,-1] # 수평이동 테이블
dy = [-1,0,1,0] # 수직이동 테이블

board = [] # 게임테이블

#게임테이블 초기화
for _ in range(m) :
  board.append(list(map(int,input().split())))

#왼쪽이동 함수 구현
def turn_left(d) :
  if d == 0 : d = 3
  else : d -= 1
  return d

#처음위치 방문
visited[x][y] = True

#게임시작
while True :
  limit = 4 # 동서남북 4번 횟수제한
  while limit > 0 : # 횟수제한
    d = turn_left(d)   # 왼쪽이동
    nx = x+dx[d] # 수평이동할 좌표 
    ny = y+dy[d] # 수직이동할 좌표
    if board[nx][ny] == 0 and not visited[nx][ny] : # 방문이 가능한 경우
      x = nx
      y = ny
      limt = 4 #횟수 초기화
      visited[x][y] = True # 방문여부확인
    else : limit -= 1 # 방문이 불가능한 경우

  #동서남북 모두 불가능하면 뒤로가기 
  nx = x-dx[d]
  ny = y-dy[d]
  if board[nx][ny] == 0 : 
    x = nx
    y = ny
  else : break #뒤로갔을때 바다이면 게임종료

#방문한 장소 개수 출력
count = 0 
for visit in visited :
  count += visit.count(True)

print(count)

    
  





