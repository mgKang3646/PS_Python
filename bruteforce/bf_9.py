
#BOJ1748 수이어쓰기1
n = int(input())

i = 1
ans = 0
while True :
  if n < 10**i : 
    ans += (n-(10**(i-1)-1))*i 
    break
  else : 
    ans += (9*(10**(i-1)))*i
    i += 1

print(ans)
    
    