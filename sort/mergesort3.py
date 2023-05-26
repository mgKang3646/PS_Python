
#입력
n = int(input())
input_list = []
for i in range(n) :
  input_list.append(input())

#병합정렬
def merge_sort(unsorted) :
  #기저조건
  if len(unsorted) <= 1 : return unsorted

  #분할 수행
  mid = len(unsorted)//2 #분할 위치
  left = unsorted[:mid] # 분할된 왼쪽
  right = unsorted[mid:] # 분할된 오른쪽

  #정렬 수행
  left_sorted = merge_sort(left) # 좌측병합정렬
  right_sorted = merge_sort(right) # 우측병합정렬

  return merge(left_sorted,right_sorted) # 병합수행

#병합수행함수
def merge(left, right) :

  leftP, rightP = 0,0
  sorted = []

  while leftP < len(left) and rightP < len(right) :

    if len(left[leftP]) < len(right[rightP]) : 
      sorted.append(left[leftP])
      leftP += 1

    elif len(right[rightP]) < len(left[leftP]) :
      sorted.append(right[rightP])
      rightP+= 1
    #문자열 길이가 같은경우
    else : 
      if left[leftP] < right[rightP] : 
        sorted.append(left[leftP])
        leftP += 1
      elif right[rightP] < left[leftP] :
        sorted.append(right[rightP])
        rightP+= 1
      else : #문자열이 같은 경우 ( 중복 제거 )
        sorted.append(left[leftP])
        leftP += 1
        rightP += 1 # 같이 넘어가주어야 중복이 방지된다. 

  # 남은 값이 있는 경우
  if leftP < len(left) : sorted += left[leftP:]
  if rightP < len(right) : sorted += right[rightP:]

  return sorted

#출력
result = merge_sort(input_list)
for i in range(len(result)) :
  print(result[i])
      
  
  
  
  