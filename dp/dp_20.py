
# 연속된 3잔을 모두 마실수 없다. 
# 많은 양의 포도주를 맛보고 싶다. ( 개 X )
# boj2156 포도주 시식

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

answer = 0
n = int(input())
arr = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1,n+1) :
    arr[i] = int(input())
  
dp[1] = arr[1]
if n >= 2 : dp[2] = arr[1] + arr[2]

for i in range(3,n+1):
    
    #OOX : i번째 와인을 안 마셨다면, i-1번째 경우의 최대값이 최대가 된다. 
    case1 = dp[i-1]
    #0X0 : i번째 와인을 마시고, i-1번째 와인을 안 마신다면, i-1번째 경우의 최대값 + i번째 와인의 양이 최대가 된다.
    case2 = dp[i-2] + arr[i]
    #X00 : i번째 와인을 마시고, i-1번째 와인을 마시고, i-2번째 와인을 안 마신다면, i-3번째 경우의 최대값 + i-1,i번째 와인의 양이 최대가 된다.
    case3 = dp[i-3] + arr[i-1] + arr[i]

    dp[i] = max(case1,case2,case3)

print(dp[n])
    