
#FIND
def find_root(parent,x) :
  if parent[x] != x : parent[x] = find_root(parent,parent[x]) 
  return parent[x]
#UNION
def union_parent(parent,a,b) :
  a_root = find_root(parent,a)
  b_root = find_root(parent,b)

  if a_root > b_root : parent[a_root] = b_root
  else : parent[b_root] = a_root


n,e = map(int,input().split()) #n:노드의 개수, e:간선의 개수
parent = [0] * (n+1) #서로소-집합테이블 생성

edges = [] #간선테이블 생성
result = 0 #총비용

#서로소-집합 테이블 초기화
for i in range(1,n+1) :
  parent[i] = i 

#간선테이블 초기화
for _ in range(e) :
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

#간선테이블 정렬
edges.sort()

#크루스칼 알고리즘 
for edge in edges :
  cost,a,b = edge # 간선 정보
  if find_root(parent,a) != find_root(parent,b) : #간선 추가시, 싸이클을 형성하지 않는경우
    union_parent(parent,a,b) # 합치기
    result += cost # 비용계산

print(result)
  

  