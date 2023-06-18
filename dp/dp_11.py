import sys 
input = sys.stdin.readline

n = int(input())
pack = [0] #팩
pack.extend(list(map(int,input().split()))) 

d= [0]*1001
d[1] = pack[1]

#BOTTOM-UP방식으로 최대비용 구하기 
for i in range(2,n+1) :
  d[i] = pack[i] # N가지 사건 중 최댓값 구하기
  for j in range(1,i) :
    d[i] = max(d[i],d[i-j] + pack[j])

#출력
print(d[n])
    
  