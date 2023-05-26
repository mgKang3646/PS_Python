n = int(input())
room = list(map(int,input().split()))

d = [0]*100 
d[0] = room[0] 
d[1] = room[1]

for i in range(2,n) :
  d[i] = max(d[i-1],d[i-2]+room[i]) # 점화식구현

print(d[n-1])