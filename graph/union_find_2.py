# 부모찾기 (FIND)
def find_root(parent,x):
  if parent[x] != x :
    parent[x] = find_root(parent,parent[x])
  return parent[x]

# 부모합치기 (UNION)
def union_graph(parent,a,b) :

  a_root = find_root(parent,a)
  b_root = find_root(parent,b)

  if a_root > b_root : parent[a] = b_root
  else : parent[b] = a_root


n,e = map(int,input().split()) # 노드의 개수 : n , 간선의 개수 : e
parent = [0]*(n+1) # 부모 테이블

#부모테이블 자기자신으로 초기화
for i in range(1,n+1) :
  parent[i] = i 

cycle = False #싸이클 플래그

#간선 입력받기
for _ in range(e) :
  a,b = map(int,input().split())

  if parent[a] == parent[b] : # 두 노드의 부모가 동일한데 간선이 추가되면 싸이클이다.
    cycle = True # 싸이클 True
    break # 반복종료

  else : union_graph(parent,a,b) #싸이클이 아닌경우 부모합치기

#출력
if cycle : print("싸이클이 발생했습니다.")
else : print("싸이클이 없습니다.")