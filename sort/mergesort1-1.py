import sys
sys.setrecursionlimit(10**6)

n = int(input())

input_arr = []
for i in range(n) :
  input_arr.append(int(input()))


def merge_sort(unsorted_arr) :
  if len(unsorted_arr) <= 1 :
    return unsorted_arr 

  mid = len(unsorted_arr)//2
  left = unsorted_arr[:mid]
  right = unsorted_arr[mid:]

  left_list= merge_sort(left)
  right_list = merge_sort(right)

  return merge(left_list,right_list)

def merge(left,right) : 
  i,j=0,0
  sorted_arr = []

  while i < len(left) and j < len(right) :
    if left[i] < right[j] :
      sorted_arr.append(left[i])
      i += 1
    else :
      sorted_arr.append(right[j])
      j += 1

  if i < len(left) : sorted_arr += left[i:]
  if j < len(right) : sorted_arr += right[j:]
    
  return sorted_arr

result = merge_sort(input_arr)

for i in range(n) :
  print(result[i])


  
  
    