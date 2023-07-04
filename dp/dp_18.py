#BOJ1912 연속합 (dp)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [ [0,0] for _ in range(n) ]

dp[0][0] = arr[0]
dp[0][1] = arr[0]

for i in range(1,n) :
  tmp = dp[i-1][1] + arr[i]
  dp[i][1] = arr[i] if arr[i] > tmp else tmp
  dp[i][0] = max(dp[i-1][0],dp[i][1])
    
print(dp[n-1][0])