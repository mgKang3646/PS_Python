import sys
input= sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n) ]
visited = [False] * n
flag = False

# 그래프 초기화
for _ in range(m) :
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# DFS 알고리즘
def dfs(index, count) :
  visited[index] = True #방문이력 True
  if count == 4 : return True # A-B-C-D-E 발견!
  for i in graph[index] : # 다른 노드로 이동
    if visited[i] : continue # 방문한 노드제외
    if dfs(i,count+1) : return True # 발견하면 탐색종료
    visited[i] = False # 발견못하면 원복

#DFS 탐색시작
for i in range(n) :
  if dfs(i,0) : # 탐색성공하면 반복종료
    flag = True
    break
  visited[i] = False #탐색실패하면 원복

#출력
if flag : print(1)
else : print(0)

    


      
  

    
  
    
    
    
