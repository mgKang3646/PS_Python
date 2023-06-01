MAX = 10000

n,m = map(int,input().split()) # n : 화폐개수, m : 목표금액
pocket = [] # 화폐구성 리스트
d = [MAX+1]*(m+1) # 최소개수 저장 테이블

# 화폐구성 입력받기
for _ in range(n) :
  pocket.append(int(input()))

# 화폐구성단위는 최소개수가 1개이므로 1 저장
for i in pocket :
  d[i] = 1

# dp 알고리즘
def do_dp(value) :
  for coin in pocket : 
    x = value - coin 
    if x < 1 : continue #0원 이하이면 제외 ( 화폐단위 X )
    d[value] = min(d[value],d[x]+1) #최솟값으로 테이블 저장

#호출
for i in range(1,m+1) :
  if d[i] > MAX : do_dp(i) #MAX보다 크면 아직 초기화가 되지 않음을 의미

#출력
if d[m] > MAX : print(-1)
else : print(d[m])
  
  




            
