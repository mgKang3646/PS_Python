#BOJ2042 구간 합 구하기
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = [0]*(n+1) # 수열
for i in range(1,n+1) :
  arr[i] = int(input())
tree = [0]*(4*n) # 세그먼트 트리

#세그먼트 트리 초기화
def init(node,start,end) :
  if start == end : #리프노드인 경우
    tree[node] = arr[start]
  else :  #리프노드가 아닌 경우
    mid = ( start + end ) // 2
    tree[node] = init(2*node,start,mid) + init(2*node+1,mid+1,end)
  return tree[node]

#세그먼트 트리 구간합 탐색하기
def sum_tree(node,start,end,fl,fr) :
  if fl > end or fr < start : return 0
  if fl <= start and fr >= end : return tree[node]
  mid = ( start + end ) // 2
  return sum_tree(2*node,start,mid,fl,fr) + sum_tree(2*node+1,mid+1,end,fl,fr)

#세그먼트 트리 UPDATE 하기
def update(node,start,end,idx,diff) :
  if start > idx or end < idx : return 
  tree[node] += diff
  if start != end :
    mid = (start + end) // 2
    update(2*node,start,mid,idx,diff)
    update(2*node+1,mid+1,end,idx,diff)

#문제풀이 시작
init(1,0,len(arr)-1) # 세그먼트 트리 초기화
for _ in range(m+k) :
  a,b,c = map(int,input().split())
  # 수정
  if a == 1 :
    diff = c - arr[b] # diff, 변경정도
    arr[b] = c # 수열에 변경내용 반영
    update(1,0,len(arr)-1,b,diff)  # 세그먼트리 변경내용 반영
  #구간합출력
  elif a == 2 :
    print(sum_tree(1,0,len(arr)-1,b,c)) # 구간합 탐색 및 출력


    
  
  
  
  
  









    
    
    