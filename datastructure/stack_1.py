import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n) :
  op = input().split()

  if op[0] == "push" :
    data = int(op[1])
    stack.append(data)

  elif op[0] == "pop" : 
    if len(stack) == 0 : print(-1)
    else : print(stack.pop())

  elif op[0] == "size" :
    print(len(stack))

  elif op[0] == "empty" :
    if len(stack) == 0 : print(1)
    else : print(0)

  elif op[0] == "top" :
    if len(stack) == 0 : print(-1)
    else : print(stack[len(stack)-1])




