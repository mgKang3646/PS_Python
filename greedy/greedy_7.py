
#BOJ1080 행렬 ( greedy )
n,m = map(int,input().split())

mx1 = [[0] for _ in range(n)] #행렬1
mx2 = [[0] for _ in range(n)] #행렬2

for i in range(n) :
  mx1[i] = list(map(int,input().rstrip("\n")))
for i in range(n) :
  mx2[i] = list(map(int,input().rstrip("\n")))

#3X3 좌표이동 리스트
dx = [0,1,2,0,1,2,0,1,2] 
dy = [0,0,0,1,1,1,2,2,2]

# 행렬 뒤집는 함수
def reverse_mx(x,y) :
  for i in range(9) :
    nx = x+dx[i]
    ny = y+dy[i] 
    mx1[ny][nx] = 1 - mx1[ny][nx] 

#두 행렬 일치여부 확인 함수
def issame() :
  for i in range(n) :
    for j in range(m) :
      if mx1[i][j] != mx2[i][j] : return False
  return True
  
#풀이
ans = 0
for i in range(n-2) : 
  for j in range(m-2) :
    if mx1[i][j] != mx2[i][j] :
      reverse_mx(j,i)
      ans += 1

#출력
if issame() : print(ans)
else : print(-1)
  
  


    



