#BOJ14202 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [ [] for _ in range(n) ]
dp[0] = [arr[0]]

for i in range(1,n) :
  for j in range(i) :
    if arr[j] < arr[i] :
      dp[i] = dp[j][:] if len(dp[j]) > len(dp[i]) else dp[i]
  dp[i].append(arr[i])


ans = []
for i in range(n) :
  ans = dp[i][:] if len(dp[i]) > len(ans) else ans

print(len(ans))
print(*ans)
  





      

