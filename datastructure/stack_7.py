import sys
input = sys.stdin.readline

n = int(input())

items = list(input().rstrip())
alpha = {}

for i in range(n) :
  alpha[chr(ord("A")+i)] = int(input())


def calculate(operator,op1,op2) :
  if operator == "+" : return op1+op2
  elif operator == "*" : return op1 * op2
  elif operator == "-" : return op1 - op2
  elif operator == "/" : return op1 / op2

stack = []

for item in items : 
  if item.isalpha() : 
    stack.append(alpha[item])
    
  else :
    op1 = stack.pop()
    op2 = stack.pop()
    result = calculate(item,op2,op1)
    stack.append(result)


result = stack.pop()
print("{:.2f}".format(round(result,3)))
    
    
    
    
    

