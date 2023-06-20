

import sys
input = sys.stdin.readline
num = input().rstrip()
n = int(input())
remote_num = [True]*10

for i in list(map(int,input().split())) :
  remote_num[i] = False

ans = []
for x in num :
  value = int(x)
  if not remote_num[value] :
    i = 1
    while True :
      if value + i < 10 and remote_num[value+i] : 
        value = value + i
        break
      elif value + i*(-1) > -1 and remote_num[value+i*(-1)] :
        value = value + i*(-1)
        break
      else : i += 1

  ans.append(str(value))

print(ans)
count_from_num = len(ans)
now = int(''.join(ans))
target = int(num)

count_from_num += abs(now-target)
count_from_100 = abs(target-100)

print(min(count_from_num,count_from_100))


  
  
  




        

      


  



  