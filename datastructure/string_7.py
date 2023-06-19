
import sys
input = sys.stdin.readline

n = list(input().rstrip())
d = [-1] *26


for i in range(len(n)) :
  value = ord(n[i]) - ord("a")
  if d[value] == -1 : d[value] = i

for i in d :
  print(i,end=" ")
  