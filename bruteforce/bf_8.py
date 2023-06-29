

#BOJ6064 카잉달력 ( math, bruteforce )
k = int(input())

# 시간초과 ( 반복문 )
def kaing_calendar(m,n,x,y) :
  a,b = 1,1
  count = 1

  while True :
    if a == x and b == y : return count 
    else :
      a = 1 if a == m else (a+1)
      b = 1 if b == n else (b+1)
      if a == 1 and b == 1 : return -1
      else : count += 1

# 시간초과 ( 재귀호출 )
def dfs(a,b,count,m,n,x,y) :
  a = 1 if a == m else (a+1)
  b = 1 if b == n else (b+1)
  if a == x and b == y : return count
  if count != 1 and a==1 and b==1 : return -1
    
  dfs(a,b,count+1,m,n,x,y)

# 정답 ( 수학 )
def kaing(m,n,x,y) :
  while x <= m*n :
    if (x-y)%n == 0 :
      return x
    x += m
  return -1
  
for _ in range(k) :
  m,n,x,y = map(int,input().split())
  print(kaing(m,n,x,y))
