
n = int(input())

def dp(value) :
  d = [0]*11 
  d[1],d[2],d[3] = 1,2,4
  for i in range(4,value+1) :
    d[i] = d[i-3]+d[i-2]+d[i-1] 
  return d[value]
  
for _ in range(n) :
  print(dp(int(input())))
  