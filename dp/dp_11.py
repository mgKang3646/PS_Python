import sys 
input = sys.stdin.readline

n = int(input())
pack = [0]
pack.extend(list(map(int,input().split())))

d= [0]*1001
d[1] = pack[1]


for i in range(2,n+1) :
  d[i] = pack[i]
  for j in range(1,i) :
    d[i] = max(d[i],d[i-j] + pack[j])


print(d[n])
    
  