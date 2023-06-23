#BOJ16194 카드구매하기2

n = int(input())
p = list(map(int,input().split()))
d = [0] * (n+1)
d[1] = p[0] 

for i in range(2,n+1) :
  d[i] = p[i-1]
  for j in range(1,i) :
    d[i] = min(d[i],d[i-j]+p[j-1])

print(d[n])
  
  
  

