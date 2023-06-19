
import sys
input = sys.stdin.readline


n,m = map(int,input().split())
parent = [0] * (n+1)

for i in range(1,n+1) :
  parent[i] = i 

#find ( 주의! 경로탐색을 줄여주는 알고리즘이지, 모든 노드의 부모를 루트로 바꾸는 로직이 아니다!!!)
def find(parent,x) :
  if parent[x] != x : parent[x] = find(parent,parent[x]) #바로 루트로 갈 수 있도록 경로축약
  return parent[x]

#union
def union(parent,a,b) :

  a_root = find(parent,a)
  b_root = find(parent,b)
  if a_root != b_root :
    if a_root > b_root : parent[a_root] = b_root
    else : parent[b_root] = a_root

for _ in range(m) :
  a,b = map(int,input().split())
  union(parent,a,b)

#결과리스트 생성
result = []
for i in range(1,n+1) :
  result.append(find(parent,i))

print(len(set(result))) #set 자료구조로 중복제거
  







