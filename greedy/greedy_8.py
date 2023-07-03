#BOJ2138 전구와 스위치 
import sys
input = sys.stdin.readline

n = int(input())
light = list(map(int,input().rstrip("\n")))
target = list(map(int,input().rstrip("\n")))

def change(light,target) :
  count = 0
  for i in range(1,n) :
    #이전 전구가 같은 상태인 경우
    if light[i-1] == target[i-1] : continue
      
    count += 1
    for j in range(i-1,i+2) :
      if j < n : light[j] = 1 - light[j]

  return count if light == target else 1e9

# 첫번째 스위치를 누르지 않은 경우
ans = change(light[:],target)

# 첫번째 스위치를 누른 경우
light[0] = 1 - light[0]
light[1] = 1 - light[1]

ans = min(ans,change(light[:],target)+1)
print( ans if ans != 1e9 else -1)

  





    