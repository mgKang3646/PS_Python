

INF = int(1e9)

n,m, start_node = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
  
for _ in range(m) :
  start,end,cost = map(int,input().split())
  graph[start][end] = cost

for middle in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1,n+1) :
      graph[start][end] = min(graph[start][end],graph[start][middle]+graph[middle][end])

max_element = -1
count = 0
for element in graph[start_node] :
    if element < INF :
      max_element = max(max_element,element)
      count += 1
  
print (count,max_element,end=" ")
    
      