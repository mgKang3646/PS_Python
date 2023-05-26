
#재귀호출을 이용함 FIND 메소드 ( 사용X )
def find_root_recursive(parent,x) :
  if parent[x] != x : parent[x] = find_root_recursive(parent,x)
  return parent[x]

#STACK + 반복문을 활용한 FIND 메소드 
def find_root_while(parent,x) :
  stack = []
  while parent[x] != x :
    stack.append(x)
    x = parent[x]

  for node in stack :
    parent[node] = x

  return parent[x]

#UNION 메소드 
def union_graph(parent,a,b) :
  a_root = find_root_while(parent,a)
  b_root = find_root_while(parent,b)

  if a_root > b_root : parent[a_root] = b_root
  else : parent[b_root] = a_root


n,m = map(int,input().split()) # n : 노드의 개수, m : 연산의 개수
parent = [0]*(n+1) # 부모 테이블 생성
graph= [[] for i in range(n+1)] # 그래프 생성

#부모 테이블 초기화
for i in range(1,n+1) :
  parent[i] = i

#그래프 입력받기
for i in range(m) :
  e,a,b = map(int,input().split())
  graph[a].append((e,b)) 

#문제 해결하기
for i in range(1,n+1) :
  for node in graph[i] :
    a = i
    e,b = node
    #합치기
    if e == 0 :
      union_graph(parent,a,b)
    #탐색
    elif e == 1 :
      a_root = find_root_while(parent,a)
      b_root = find_root_while(parent,b)
    
      if a_root == b_root : print("YES")
      else : print("NO")