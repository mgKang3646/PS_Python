# 루트 탐색 ( Find )
def find_root(parent,x) :
  if parent[x] != x : return find_root(parent,parent[x])
  else : return x

# 간선 합치기 ( Union )
def union_graph(parent,a,b) :

  a_root = find_root(parent,a)
  b_root = find_root(parent,b)
  # 값이 작으면 루트
  if a_root > b_root : parent[a] = b_root
  elif b_root > a_root : parent[b] = a_root


n,e = map(int,input().split()) #노드의 개수 : n , 간선의 개수 : e
parent = [0] * (n+1) # 서로소 집합 테이블

# 서로소 집합 테이블 초기화
for i in range(1,n+1) :
  parent[i] = i

# Union-Find 알고리즘 시작
for _ in range(e) :
  a,b = map(int,input().split()) #간선 입력받기
  union_graph(parent,a,b) # 간선 합치기 


# 루트 노드 출력
print("각 노드의 루트노드 출력 :  ",end=' ')
for i in range(1,n+1) :
  print(find_root(parent,i),end=' ')

print()

# 부모 노드 출력
print("각 노드의 부모노드 출력 :  ",end=' ')
for i in range(1,n+1) :
  print(parent[i],end=' ')