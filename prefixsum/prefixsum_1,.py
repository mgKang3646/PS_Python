


import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
sum = [0]*(n+1)

for i in range(1,n+1) :
  sum[i] = sum[i-1] + arr[i-1] 

for _ in range(m) : 
  i,j = map(int,input().split())
  result = sum[j] - sum[i-1]
  print(result)