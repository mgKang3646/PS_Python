

#BOJ11399 ATM

import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int,input().split()))
time.sort()

time_sum = [0]*(n)
time_sum[0] = time[0]

for i in range(1,n) :
  time_sum[i] = time_sum[i-1] + time[i] 

print(sum(time_sum))