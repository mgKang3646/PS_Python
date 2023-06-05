
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
flag = True
current = 0

for _ in range(n) :
  value = int(input())
  while current < value :
    current += 1
    result.append("+")
    stack.append(current)
  if stack[-1] == value :
    stack.pop()
    result.append("-")
  else : 
    flag = False
    break

if flag :
  for op in result :
    print(op)
else :
  print("NO")

    
  

  
