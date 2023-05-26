N = int(input())
sortArr = []

for i in range(N) :
  sortArr.append(int(input()))


for i in range(N) :
  lastIndex = 0 
  for j in range(N-1,i,-1) :
    if sortArr[j] < sortArr[j-1] :
      sortArr[j], sortArr[j-1] = sortArr[j-1], sortArr[j]
      lastIndex = j
  i = lastIndex-1 
  # 마지막으로 변환 인덱스의 앞 까지는 정렬이 완료 (lastIndex-1)
  # lastIndex는 한번 더 정렬될 가능성이 있다.


for i in  range(n) :
  print(sortArr[i])