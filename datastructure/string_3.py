import sys
input = sys.stdin.readline

data = list(input().strip("\n"))
cursor = len(data)
n = int(input())

def editor(data,op) : 
    global cursor
    if op[0] == "P" :
      data.insert(cursor,op[1]) #O(N) 시간초과발생
      cursor += 1
      
    elif op[0] =="L" :
      if cursor != 0 : cursor -= 1
      
    elif op[0] == "D" :
      if cursor != len(data) : cursor += 1
        
    elif op[0] == "B" :
      if cursor != 0 :
        del data[cursor-1] #O(N) 시간초과발생
        cursor -= 1

for _ in range(n) :
  op = input().split()
  editor(data,op)

for value in data :
  print(value,end="")
    



