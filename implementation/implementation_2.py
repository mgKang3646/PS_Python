
n,m = map(int,input().split())
x,y,d = map(int,input().split())
graph = []
visited = [[False] * (n) for i in range(m)]
for _ in range(m) :
    graph.append(list(map(int,input().split())))

direction = [[0,-1],[1,0],[0,1],[-1,0]]
left = [3,0,1,2]
count = 1

def gilsearch(x,y,d) :
    for _ in range(4) : 
      global count
      visited[x][y] = True
      next = left[d]
      move = direction[next]
      if graph[x+move[0]][y+move[1]] == 0 and not visited[x+move[0]][y+move[1]]  : 
          count += 1
          gilsearch(x+move[0],y+move[1],next)
      else : d = next


gilsearch(x,y,d)
print(count)

    


   


  


