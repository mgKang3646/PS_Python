  
def isvalidate(direct) :
  dx,dy = direct
  if  x+dx >= 1 and x+dx <= 8 and y+dy >= 1 and y+dy <= 8 : return True
  else : False

n = input()
x, y = ord(n[0]), int(n[1])
x = x - ord('a') + 1 #y와 맞추어주기

direction = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[-1,-2],[1,-2]]
result = 0 

for direct in direction :
  if isvalidate(direct) : result += 1

print(result)



  




