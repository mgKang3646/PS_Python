
import sys
input = sys.stdin.readline

n = int(input())

box = [[] for _ in range(n)]

for i in range(n) :
  box[i] = list(input().rstrip())

def max_candy(box) :
  max_count = 0
  count = 1
  
  for i in range(n) :
    for j in range(1,n) :
      if box[i][j] == box[i][j-1] : 
        count += 1
      else :
        max_count = max(max_count,count)
        count = 1
    max_count = max(max_count,count)
    count = 1        

    for j in range(1,n) :
      if box[j][i] == box[j-1][i] :
        count += 1
      else : 
        max_count = max(max_count,count)
        count = 1
    max_count = max(max_count,count)
    count = 1
    
  return max_count 

max_count = max_candy(box)

for i in range(n) :
  for j in range(1,n) :
    box[i][j-1],box[i][j] = box[i][j],box[i][j-1] #변경
    max_count = max(max_count,max_candy(box))
    box[i][j-1],box[i][j] = box[i][j],box[i][j-1] #원복

  for j in range(1,n) :
    box[j-1][i],box[j][i] = box[j][i],box[j-1][i] #변경
    max_count = max(max_count,max_candy(box))
    box[j-1][i],box[j][i] = box[j][i],box[j-1][i] #원복

print(max_count)



    
    

    



  

  



