n = int(input())

sortArr = []
for i in range(n):
  sortArr.append(int(input()))

def quickSort(left, right) :
  pLeft = left
  pRight = right
  pivot = sortArr[ int((right+left)/2) ]

  while True:
    while sortArr[pLeft] <= pivot : pLeft += 1 
    while sortArr[pRight] > pivot  : pRight -= 1

    if pLeft < pRight :
      sortArr[pLeft], sortArr[pRight] = sortArr[pRight],sortArr[pLeft]
    else : break

  
  print(left,right,pLeft,pRight)
  if left < pRight : quickSort(left,pRight)
  if pLeft < right : quickSort(pLeft,right)


quickSort(0,n-1)

for i in range(n):
  print(sortArr[i])
      
    
    
  