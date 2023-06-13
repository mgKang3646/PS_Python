import sys
input= sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n) ]
visited = [False] * n
flag = False

for _ in range(m) :
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(index, count) :
  visited[index] = True
  if count == 4 : return True
  for i in graph[index] :
    if visited[i] : continue
    if dfs(i,count+1) : return True
    visited[i] = False

for i in range(n) :
  if dfs(i,0) :
    flag = True
    break
  visited[i] = False
    
if flag : print(1)
else : print(0)

    

# 재귀호출에 대한 이해부족  
# 방문이력이 필요하다는 생각 X
# 방문이력을 풀어줘야 한다는 생각 x
# 양방향 관계임을 인지 X
      
  

    
  
    
    
    
