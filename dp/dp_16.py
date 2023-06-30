#BOJ11053 가장 긴 증가하는 부분수열

n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n

for i in range(n) :
  for j in range(i) :
    if arr[i] > arr[j] :
      dp[i] = max(dp[i],dp[j])

  dp[i] += 1

print(max(dp))
    
    
    



