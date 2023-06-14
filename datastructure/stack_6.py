
import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int,input().split()))

f = [0] * 1000001
d = [-1] * n
for item in items :
  f[item] += 1

stack = []

for pointer in range(n) :
  while stack :
    if f[items[stack[-1]]] >= f[items[pointer]] : break
    d[stack.pop()] = items[pointer]
  stack.append(pointer)

for value in d :
  print(value,end= " ")
    







