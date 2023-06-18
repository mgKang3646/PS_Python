
import sys
input = sys.stdin.readline

items = list(input().rstrip())
stack = []
stack.append(items[0])

raiser_count = 0
block_count = 0

for i in range(1,len(items)) :
  if items[i] == "(" :
    stack.append(items[i])

  elif items[i] == ")" :
    if items[i-1] == "(" : 
      stack.pop()
      block_count += len(stack) 
    else :
      stack.pop()
      block_count += 1

print(block_count)


    
  