
import sys
input = sys.stdin.readline

n = int(input())
box = [[] for _ in range(n)]

#사탕상자 초기화
for i in range(n) :
  box[i] = list(input().rstrip())

# 연속된 같은 색상 사탕개수의 최댓값을 파악하는 함수
def max_candy(box) :
  max_count = 0
  count = 1
  
  for i in range(n) :
    for j in range(1,n) : # 행탐색
      if box[i][j] == box[i][j-1] :  #색상이 같은 경우
        count += 1
      else : # 색상이 다른 경우
        max_count = max(max_count,count)
        count = 1
    max_count = max(max_count,count)
    count = 1        

    for j in range(1,n) : #열탐색
      if box[j][i] == box[j-1][i] : # 색상이 같은 경우
        count += 1
      else : # 색상이 다른 경우
        max_count = max(max_count,count)
        count = 1
    max_count = max(max_count,count)
    count = 1
    
  return max_count 

# 교환시작
max_count = max_candy(box)

for i in range(n) :
  for j in range(1,n) : # 행탐색
    box[i][j-1],box[i][j] = box[i][j],box[i][j-1] #변경
    max_count = max(max_count,max_candy(box))
    box[i][j-1],box[i][j] = box[i][j],box[i][j-1] #원복

  for j in range(1,n) : # 열탐색
    box[j-1][i],box[j][i] = box[j][i],box[j-1][i] #변경
    max_count = max(max_count,max_candy(box))
    box[j-1][i],box[j][i] = box[j][i],box[j-1][i] #원복

#출력
print(max_count)



    
    

    



  

  



