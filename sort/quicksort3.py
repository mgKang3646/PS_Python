# 입력
n = int(input())

input_list = []
for i in range(n) :
  input_list.append(input())  

# 퀵소트 함수
def quicksort(unsorted) :
  # 리스트에 아이템이 1개 이하인 경우 ( 기저조건 )
  if len(unsorted) <=1 : return unsorted

  pivot = unsorted[0] # 기준값
  left = [] # 왼쪽 리스트 
  right = [] # 우측 리스트

  # 기준값보다 작으면 left에 크면 right에 append
  for i in range(1,len(unsorted)) :
    if len(pivot) > len(unsorted[i]) : left.append(unsorted[i])
    elif len(pivot) < len(unsorted[i]) : right.append(unsorted[i])
    else : # 문자열 길이가 같은 경우
      if pivot > unsorted[i] : left.append(unsorted[i])
      elif pivot < unsorted[i] : right.append(unsorted[i])
      # 문자열이 같은 경우, left와 right 에 넣어주지 않아 자동으로 중복제거
      
  return quicksort(left) + [pivot] + quicksort(right)

#출력
result = quicksort(input_list)
for i in range(len(result)) :
  print(result[i])
  
  
  