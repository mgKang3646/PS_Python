

n = int(input())
INF = int(1e9)
d = [INF]*(n+1)

d[1] = 0

for i in range(2,n+1) :
  items = []
  if i%3 == 0 :
    items.append(i//3)
  if i%2 == 0 :
    items.append(i//2) 

  min_value = d[i-1]
  for item in items :
    min_value = min(min_value,d[item])

  d[i] = min_value + 1


print(d[n])

  
    

  