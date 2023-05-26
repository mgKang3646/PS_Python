
#입력받기
n = int(input())

input_list = []
for i in range(n) :
  input_list.append(input())

#문자열 비교함수
def is_smaller(value,target) :
  if len(value)<len(target) : return True
  elif len(value) > len(target) : return False
  else : 
    if value < target : return True
    elif value > target : return False
    else : return True

# 힙소트
def heap_sort(unsorted) :
  #힙트리생성
  last_child = len(unsorted)-1
  last_parent = (last_child-1)//2 

  # 가장 마지막 부모부터 루트까지 힙트리 생성하기
  for i in range(last_parent,-1,-1) :
    heapify(unsorted,i) 
    
  #힙정렬 
  sorted = []
  for i in range(len(unsorted)-1,-1,-1) : 
    unsorted[i], unsorted[0] = unsorted[0],unsorted[i] # 루크와 가장 마지막 값 스위칭
    value = unsorted.pop(i) # 마지막 위치값 pop하여 정렬리스트에 추가하기
    if value not in sorted : sorted.append(value) # not in으로 중복 확인하여 추가하기
    if i != 0 : heapify(unsorted,0) # i=0이면 더이상 unsorted에 정렬할 item이 없음

  return sorted

#힘트리 생성 함수
def heapify(unsorted,index) :
  pointer = index
  pivot = unsorted[pointer]

  while pointer <= ((len(unsorted)-1)-1)//2 : #가장 마지막 부모까지 반복
    #좌측, 우측 중 큰값을 가진 자식 고르기
    left_child = 2*pointer+1
    right_child = left_child+1
    child = ( right_child if right_child < len(unsorted) and is_smaller(unsorted[right_child],unsorted[left_child]) else left_child )

    #부모와 자식 값 비교하여 최솟값을 부모로 올리기 
    if is_smaller(pivot,unsorted[child]) : break #부모가 최솟값이므로 반복종료
    else : # 자식이 최솟값이므로 자식을 부모로 올리기
      unsorted[pointer] = unsorted[child]
      pointer = child # 부모였던 값은 자식으로 내려가기

  unsorted[pointer] = pivot  #현재 위치에 값을 저장하고 힙트리생성함수 종료

#출력
result = heap_sort(input_list)
for i in range(len(result)) :
  print(result[i])
