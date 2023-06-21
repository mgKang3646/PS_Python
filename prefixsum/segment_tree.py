

arr = list(map(int,input().split())) #수열
tree = [0]*(len(arr)*4) #세그먼트트리

#세그먼트트리 구현
def init_tree(start,end,node) :
  if start == end : #리프노드인 경우
    tree[node] = arr[start]
    return tree[node]
  #리프노드가 아닌경우
  mid = (start+end)//2 #이진탐색
  tree[node] = init_tree(start,mid,2*node) + init_tree(mid+1,end,2*node+1) #재귀호출
  return tree[node]

init_tree(0,len(arr)-1,1)
print(tree)
  




           