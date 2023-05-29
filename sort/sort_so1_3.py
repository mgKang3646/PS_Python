


n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() #오름차순
b.sort(reverse=True) #내림차순
 
for i in range(k) : #최대 k번 바꿔치기
  if a[i] < b[i] :  # b가 큰 경우에 바꿔치기
    a[i],b[i] = b[i],a[i] 
  else : break # b가 a보다 작으면 a는 오름차순, b는 내림차순이기에 이후는 a가 b보다 항상 크다. 그러므로 반복 종료

print(sum(a))