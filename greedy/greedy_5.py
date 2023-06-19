import sys
input = sys.stdin.readline

n = int(input())
meetings = [[] for _ in range(n)]

for i in range(n) :
  start,end = map(int,input().split())
  meetings[i] = [start,end]

meetings = sorted(meetings,key=lambda time : (time[1],time[0]))

count = 1
end = meetings[0][1]
for i in range(1,n) :
  if end > meetings[i][0] : continue
  end = meetings[i][1] 
  count+=1

print(count)
      

  


  
  