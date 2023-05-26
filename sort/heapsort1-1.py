import sys
sys.setrecursionlimit(10**6)

n = int(input())

input_list = []
for i in range(n) :
  input_list.append(int(input()))

def heap_sort(unsorted) :

  last_child_index = len(unsorted)-1
  last_parent_index = (last_child_index - 1)//2
  #힙트리 생성하기
  for i in range(last_parent_index,-1,-1) :
    doheap(unsorted, i)

  #힙정렬하기
  sorted = []
  for i in range(last_child_index,-1,-1) :
   unsorted[0], unsorted[i] = unsorted[i], unsorted[0] 
   sorted.append(unsorted.pop(i))
   if i != 0 : doheap(unsorted,0)

  return sorted
    
def doheap(unsorted, parent) : 
  pivot = unsorted[parent]
  pointer = parent

  
  while pointer <= ((len(unsorted)-1)-1)//2 :
    #left, right 자식 중 가장 큰값 찾기 
    left = 2*pointer+1
    right = left+1
    child = left
    if right < len(unsorted) and unsorted[right] > unsorted[left]  : child = right

    #비교하기
    if pivot > unsorted[child] : break;
    else : 
      unsorted[pointer] = unsorted[child]
      pointer = child

  unsorted[pointer] = pivot

#출력
result = heap_sort(input_list)
for i in range(n-1,-1,-1) :
  print(result[i])

  




      
    
    



    
  
    
    
  
  