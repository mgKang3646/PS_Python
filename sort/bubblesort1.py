N = int(input())
sortArr = []

for i in range(N) :
  sortArr.append(int(input()))


for i in range(N) :
  changeCount = 0
  for j in range(N-1,i,-1) :
    if sortArr[j] < sortArr[j-1] :
      sortArr[j], sortArr[j-1] = sortArr[j-1], sortArr[j]
      changeCount += 1
  if changeCount == 0 :
    break

for i in range(len(sortArr)) :
  print(sortArr[i])
    
    
    

