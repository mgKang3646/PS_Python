import sys
sys.setrecursionlimit(10**6)

n = int(input())

input_arr = []
for i in range(n) :
  input_arr.append(int(input()))

#mersort시작
def merge_sort(left,right) :
  if left < right : #해당 코드를 까먹은 이유는????
    center = int((left+right)/2)
    #분할시작
    merge_sort(left,center)
    merge_sort(center+1,right)
  
    #정렬시작
    do_sort(left,right)

def do_sort(left,right) :
  
  #임시배열생성
  buff = []
  center = int((left+right)/2) 

  #비교를 위한 포인터 생성
  buff_pointer = 0 #임시배열포인터
  right_pointer = center + 1 #우측배열포인터
  arr_pointer = left
  
  #left배열을 임시배열에 복사
  buff = input_arr[left : center+1] # 끝은 +1을 해주어야 center 이전까지 복사된다.

  #정렬 시작
  while buff_pointer < len(buff) and right_pointer <= right :
      leftvalue = buff[buff_pointer]
      rightvalue = input_arr[right_pointer]
      if leftvalue < rightvalue : 
        input_arr[arr_pointer] = leftvalue 
        buff_pointer += 1
      else : 
        input_arr[arr_pointer] = rightvalue
        right_pointer += 1
      arr_pointer += 1
    
  while buff_pointer < len(buff) :
    input_arr[arr_pointer] = buff[buff_pointer]
    arr_pointer += 1
    buff_pointer += 1

#병합정렬 호출
merge_sort(0,n-1)

#출력
for i in range(n) :
  print(input_arr[i])
      

  


  