import sys
input = sys.stdin.readline


stack1= list(input().rstrip())
stack2 = []

n = int(input())

for _ in range(n) :
  op = input().split()
  if op[0] == "P" : stack1.append(op[1])
  elif op[0] == "L" : 
    if stack1 : stack2.append(stack1.pop())
  elif op[0] == "D" : 
    if stack2 : stack1.append(stack2.pop())
  elif op[0] == "B" : 
    if stack1 : stack1.pop()

while stack2 :
  stack1.append(stack2.pop())

for value in stack1 :
  print(value,end="")

