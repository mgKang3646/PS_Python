
from collections import deque
import copy
import sys
input = sys.stdin.readline


n = int(input())
indegrees = [0]*(n+1)
time = [0]*(n+1)
graph = [[] for _ in range(n+1)] 

for i in range(1,n+1) :
  info = list(map(int,input().split()))
  time[i] = info[0]

  for j in range(1,len(info)) :
    sunsu = info[j]

    if sunsu != -1 : 
      graph[sunsu].append(i)
      indegrees[i] += 1
    else : break

q = deque()
for i in range(1,n+1) :
  if indegrees[i] == 0 : q.append(i)

result = copy.deepcopy(time) #값복사 

while q :
  now = q.popleft()
  for next in graph[now] : 
    result[next] = max(result[next],result[now] + time[next]) #다른 선수과목과 비교하여 큰값을 테이블에 저장하기
    indegrees[next] -= 1
    if indegrees[next] == 0 : q.append(next)

for i in range(1,n+1) :
  print(result[i])







  
  



