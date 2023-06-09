
from collections import deque
import sys
input = sys.stdin.readline

result = []
stack = []
q = deque(list(input().rstrip()))

while q :
  char = q.popleft();

  if char == "<" :
    result.append(char)
    while char != ">"  :
      char = q.popleft()
      result.append(char)

  elif char == " " : result.append(char)
    
  else : 
    stack.append(char)
    while q[0] != " " and q[0] != "<" :
      char = q.popleft()
      stack.append(char)
      if not q : break

    while stack :
      result.append(stack.pop())

print("".join(result)[:])


      
      
      
      