
MAX = 10000

n,m = map(int,input().split())
money_basic = []
money_table =[MAX+1]*(m+1)

for _ in range(n) :
  money_basic.append(int(input()))

for money in money_basic :
  money_table[money] = 1

def calculate(value) :
  min_money = MAX+1
  for money in money_basic :
    x = value - money
    if x < 1 : continue
    if min_money > money_table[x] : min_money = money_table[x] + 1
  return min_money  

for i in range(1,m+1) :
  if money_table[i] > MAX : 
    money_table[i] = calculate(i)

if money_table[m] > MAX : print(-1)
else : print(money_table[m])
  
  




            
