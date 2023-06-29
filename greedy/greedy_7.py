
#BOJ1080 행렬 ( greedy )
n,m = map(int,input().split())

mx1 = [[0] for _ in range(n)]
mx2 = [[0] for _ in range(n)]

for i in range(n) :
  mx1[i] = list(map(int,input().rstrip("\n")))
for i in range(n) :
  mx2[i] = list(map(int,input().rstrip("\n")))

dx = [0,1,2,0,1,2,0,1,2]
dy = [0,0,0,1,1,1,2,2,2]

def isvalidate(x,y) :
  if x >=0 and y>=0 and x<m and y<n : return True
  else : return False

#일치여부 확인
def issame() :
  for i in range(n) :
    for j in range(m) :
      if mx1[i][j] != mx2[i][j] : return False
  return True

#뒤집기
def reverse_mx(x,y) :
  for i in range(9) :
    nx = x+dx[i]
    ny = y+dy[i] 
    mx1[ny][nx] = 1 - mx1[ny][nx] 

count = 0
for i in range(n-2) :
  for j in range(m-2) :
    if mx1[i][j] != mx2[i][j] :
      reverse_mx(j,i)
      count += 1

if issame() : print(count)
else : print(-1)
  
  


    



