#BOJ1699 제곱수의 합
n = int(input())
dp = [0] * (n+1)

for i in range(1,n+1) :
  tmp = []
  for j in range(1,i+1) :
    if i < j**2 : break
    tmp.append(dp[i-j**2]+1)
  dp[i] = min(tmp) if tmp else 1

print(dp[n])

