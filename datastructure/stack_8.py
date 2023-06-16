import sys
input = sys.stdin.readline

infix = list(input().rstrip()) 
postfix = [] # 후위표기식 
stack = [] # 연산자 스택
priority = {'+': 1 , '-' : 1, '*' : 2, '/' : 2,'(': 0} # 우선순위 딕셔너리


for x in infix :
  if x.isalpha() : postfix.append(x) # 문자인 경우 바로 출력
  elif x == "(" : stack.append(x) # ( 이면 바로 STACK에 PUSH
  elif x == ")" : 
    while stack[-1] != "(" : # ) 나오면 이후, 연산자는 우선순위가 무조건 낮으므로 ( 를 만날때까지 POP
      postfix.append(stack.pop())
    stack.pop()
  else : # 괄호가 아닌 연산자인 경우
    while stack and priority[x] <= priority[stack[-1]] : # 우선순위가 STACK의 TOP 연산자보다 낮은 경우
      postfix.append(stack.pop()) # 높은 우선순위를 가진 연산자 모두 POP
    stack.append(x) # 우선순위 높은 연산자가 이제 없으므로 PUSH

#남은 연산자 마지막으로 POP ( 털기 )
while stack : postfix.append(stack.pop())

#출력
for value in postfix :
  print(value,end="")
      