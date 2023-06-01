

def find_root(parent,x) :
  if parent[x] != x  : parent[x] = find_root(parent,parent[x])
  return parent[x]

def union_graph(parent,a,b) :
  a_root = find_root(parent,a)
  b_root = find_root(parent,b)

  if a_root > b_root : parent[a_root] = b_root
  else : parent[b_root] = a_root


n,m = map(int,input().split())
lines = []
parent = [0] * (n + 1)

for i in range(1,n+1) :
  parent[i] = i

for _ in range(m) :
  a,b,cost = map(int,input().split())
  lines.append((a,b,cost))

lines = sorted(lines,key=lambda line : line[2])

total = 0
last = 0
for line in lines :
  a,b,cost = line

  if find_root(parent,a) == find_root(parent,b) : continue #같은 싸이클

  union_graph(parent,a,b)
  total += cost
  last = cost

print(total-last)
  












  