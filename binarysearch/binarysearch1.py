
# 입력받기
n = int(input())
items = list(map(int, input().split()))
m = int(input())
items_search = list(map(int,input().split())) 

# 이진탐색을 위한 리스트 정 렬
items.sort()

# 이진탐색
def binary_search(target, start, end) :
  #기저조건 
  mid = (start + end )//2
  if start > end : return False # 탐색실패
  if items[mid] == target : return True # 탐색성공
    
  # 재귀함수 호출 
  if items[mid] > target : 
    return binary_search(target,start,mid-1) 
  else : 
    return binary_search(target,mid+1,end)

# 이진탬색 시작
for target in items_search :
  if binary_search(target,0,n-1):
    print('yes', end=' ')
  else :  print('no', end=' ')


  




