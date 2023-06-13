import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) # 수열 테이블
result = [-1] * (n) #결과 테이블

stack = [] #스택테이블
stack.append(0) # 인덱스를 STACK에 저장
i = 1 # 오큰수 포인터

while stack and i < n :
  while stack and  arr[stack[-1]] < arr[i] : # 오큰수인 경우
    result[stack[-1]] = arr[i]  # 결과저장
    stack.pop() # STACK에서 제거 
    
  stack.append(i) # 다음 인덱스 STACK에 추가
  i += 1 # 오큰수 포인터 이동

#출력
for value in result :
  print(value, end=" ")
  




    
  
  
  
    
  
