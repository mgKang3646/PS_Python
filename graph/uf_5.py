
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [0] * (n+1)

#부모테이블 초기화
for i in range(1,n+1) :
  parent[i] = i 

#find 
def find(parent,x) :
  if parent[x] != x : parent[x] = find(parent,parent[x]) #바로 루트로 갈 수 있도록 경로압축
  return parent[x]

#union
def union(parent,a,b) :
  a_root = find(parent,a)
  b_root = find(parent,b)
  if a_root != b_root : 
    if a_root > b_root : parent[a_root] = b_root
    else : parent[b_root] = a_root

#UNION-FIND 알고리즘 시작
for _ in range(m) :
  a,b = map(int,input().split())
  union(parent,a,b)

#결과리스트 생성
result = []
for i in range(1,n+1) :
  result.append(find(parent,i))

print(len(set(result))) #set자료구조로 중복제거
  







