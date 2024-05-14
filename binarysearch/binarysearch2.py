# 입력 받기
n, m = map(int,input().split())
items = list(map(int,input().split()))

# 리스트 정렬
items.sort()

# 절단기 높이로 얻을 수 있는 총 떡의 길 이
def get_high(pivot) :
  high = 0

  for value in items :
    if pivot < value :
      high += value - pivot
  return high 

# 최적 절단기높이를 출력하는 이진탐색함수
def binary_search(target, start, end, max_high) :
  mid = (start + end)//2 # 절단기높이
  h = get_high(mid) # 결과

  # 기저함수
  if start > end : return max_high #탐색실패
  if target == h : return mid  #탐색성공

  # 재귀함수 호출
  # 1) 결과가 목표보다 부족한 경우 
  # max_high는 그대로 유지
  if target > h : return binary_search(target,start,mid-1,max_high)
  # 2) 결과가 목표보다 큰 경우
  # max_high는 현재 절단기 높이로 초기화
  else : return binary_search(target,mid+1,end,mid) 

# 최적 절단기높이 탐색함수 호출
result = binary_search(m,items[0],items[n-1],0)
print(result)
  
  