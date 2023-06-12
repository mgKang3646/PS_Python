
from collections import deque

MAX = 1000000
n,k = map(int,input().split())
d = [0] * (MAX+1)

def bfs(start,target) :
  q = deque()
  q.append(start)

  while q :
    value = q.popleft()
    if value == target : break
    else :
      for next in (value+1,value-1,value*2) :
        if 0 <= next <= MAX and not d[next] :
          d[next] = d[value] + 1
          q.append(next)
      
  return d[value]
      

print(bfs(n,k))

  
    


      
