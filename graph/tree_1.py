
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

def char_num(char) :
  return ord(char) - ord("A")

def num_char(num) :
  return chr(num + ord("A"))

for i in range(n) :
  parent,left,right = map(char_num, input().split())
  graph[parent] = [left,right]


def traversal(graph,type) :
  stack = [0]
  visited = [False] * 26
  while stack :
    value = stack.pop()
    if visited[value] : print(num_char(value),end="")
    else : 
      visited[value] = True
      sub = []
      if type == "preorder" : sub = [ graph[value][1],graph[value][0],value ]
      elif type == "inorder" : sub = [ graph[value][1],value,graph[value][0] ]
      else : sub = [ value, graph[value][1],graph[value][0] ]

      for i in sub :
        if i != char_num(".") : stack.append(i)

      
traversal(graph,"preorder")
print()
traversal(graph,"inorder")
print()
traversal(graph,"postorder")

    
      
  
  


