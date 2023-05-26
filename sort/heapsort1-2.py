import sys
sys.setrecursionlimit(10**6)

n = int(input())

input_list = []
for i in range(n) :
  input_list.append(int(input()))

def heap_sort(unsorted) :

  #힙트리 생성하기
  last_child_index = len(unsorted)-1 # 힙트리의 마지막 자식 인덱스
  last_parent_index = (last_child_index - 1)//2 # 힙트리의 마지막 부모 인덱스
  for i in range(last_parent_index,-1,-1) : # 모든 부모인덱스를 돌며 힙트리 생성, 밑(마지막부모인덱스)에서부터 생성되어야 root 자리에 최대값이 올라온다.
    doheap(unsorted, i)

  #힙정렬하기
  sorted = []
  for i in range(last_child_index,-1,-1) :
   unsorted[0], unsorted[i] = unsorted[i], unsorted[0] #root와 끝자리 swap
   sorted.append(unsorted.pop(i)) # 이미 정렬된 끝자리 제거하기
   if i != 0 : doheap(unsorted,0) # swap으로 인해, 힙트리가 깨졌으므로 다시 힙트리 생성

  return sorted

#힙트리는 완전이진트리이며 부모가 자식보다 크다. 그러므로 부모를 기준으로 해당 조건을 맞춘다.
def doheap(unsorted, pivotIndex) : 
  pivot = unsorted[pivotIndex] # 힙트리 생성의 기준값
  pointer = pivotIndex # 힙트리 생성의 기준인덱스
  
  while pointer <= ((len(unsorted)-1)-1)//2 :
    # 자식 left와 자식 right 중 큰 값을 child로 지정 (완전이진트리)
    left = 2*pointer+1
    right = left+1
    child = left
    if right < len(unsorted) and unsorted[right] > unsorted[left]  : child = right

    #비교하기
    if pivot > unsorted[child] : break; # 부모가 자식보다 크므로 반복문 종료
    else : #자식이 부모보다 큰 경우
      unsorted[pointer] = unsorted[child] # 부모자리에 자식이 올라가고 쟈식자리에는 부모였던 값이 내려온다.
      pointer = child # 자식인덱스에 부모였던 값이 내려왔으므로, 자식의 자식과 다시 비교해야한다.

  unsorted[pointer] = pivot #반복문이 종료되면 기준인덱스에 기준값을 넣는다. 

#출력
result = heap_sort(input_list)
for i in range(n-1,-1,-1) : #오름차순 출력
  print(result[i])

  




      
    
    



    
  
    
    
  
  