import sys
sys.setrecursionlimit(10**6)

x = int(input())
d = [0]*30001

def calculate(x) :
  # 기저조건 
  if x == 1 : return 0

  # 재귀호출
  if x > 1 : 
    d[x] = calculate(x-1)+1
  if x % 5 == 0 : 
    d[x] = min(d[x],calculate(x//5)+1)
  if x % 3 == 0 : 
    d[x] = min(d[x],calculate(x//3)+1)
  if x % 2 == 0 : 
    d[x] = min(d[x],calculate(x//2)+1)

  return d[x]

print(calculate(x))
  