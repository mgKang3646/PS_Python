
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
wallet = []

for _ in range(n) :
  coin = int(input().rstrip())
  if coin > k : break
  wallet.append(coin)

count = 0
while k != 0 :
  coin = wallet.pop()
  if coin <= k :
    count += k//coin
    k = k%coin

print(count)
  
  