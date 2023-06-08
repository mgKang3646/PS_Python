

n,m = map(int,input().split())

def GCD (x,y) :
  while(y) : 
    x,y = y,x%y
  return x

def LCM (x,y) :
  return (x*y)//GCD(x,y)

print(GCD(n,m))
print(LCM(n,m))