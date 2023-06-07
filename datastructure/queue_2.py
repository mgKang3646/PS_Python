from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
q = deque([ x for x in range(1,n+1)])
result = []

count = 1 
while q :
  if count == k :  # K번째이면 POP하기
    result.append(q.popleft())
    count = 1
  else : # K번째가 아니면 POP하고 다시 PUSH하기
    q.append(q.popleft())
    count += 1

print("<",", ".join(list(map(str,result))),">", sep='') # sep='' 공백을 없애고 ", " 구분자로 출력하기
    
  




      