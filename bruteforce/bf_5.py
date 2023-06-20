import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(input().split())
  
ans = abs(target-100)

for x in range(1000001) :
  now = str(x)
  for i in range(len(now)) :
    if now[i] in broken : break
    if i == len(now)-1 :
      ans = min(ans,abs(target-int(now))+len(now))
      
print(ans)