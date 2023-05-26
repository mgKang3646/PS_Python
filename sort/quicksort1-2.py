# BOJ 재귀호출 깊이가 1000이 한계이므로 재귀호출 깊이 늘려주기
import sys
sys.setrecursionlimit(10**6)

# 입력받기
n = int(input())
inputList = []

for i in range(n) :
  inputList.append(int(input()))

# 퀵소트 함수
def quickSort(tmpList) :
  # 더 이상 정렬할 값이 없는 경우
  if len(tmpList) <= 1 :
    return tmpList
  
  pivot = tmpList[0] # 피벗
  left = [ value for value in tmpList[1:] if value < pivot]
  right = [ value for value in tmpList[1:] if value > pivot ]

  # left, right = [], [] # 왼쪽, 오른쪽 리스트 생성
  # for value in tmpList[1:] :
  #   if value < pivot : left.append(value) # pivot보다 작은 경우, left에 삽입
  #   else : right.append(value) # pivot보다 큰 경우, right에 삽입

  return quickSort(left) + [pivot] + quickSort(right) # 반환

# 퀵소트 함수 호출
resultList = quickSort(inputList)

#출력
for i in range(n) :
  print(resultList[i])
