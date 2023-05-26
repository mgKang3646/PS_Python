#입력받기
n = int(input())
unsorted = []
for i in range(n) :
  unsorted.append(input())

# 문자열 길이 비교 함수
def is_bigger(value1, value2) :
  if len(value1) > len(value2) : return True
  elif len(value1) < len(value2) : return False
  else :  #문자열 길이가 같은 경우
    if value1 > value2 : return True
    elif value1 < value2 : return False
  

for i in range(len(unsorted)) :
  for j in range(len(unsorted)-1,i,-1) :
    #두 문자열이 같은 경우
    if unsorted[j] == unsorted[j-1] : 
      unsorted.pop(j) #문자열 하나 제거
      continue # 같은 문자열인 j-1에서 비교를 하기 위해, continue로 진행
    # 문자열 비교 후 swap
    if not is_bigger(unsorted[j],unsorted[j-1]) :
      unsorted[j], unsorted[j-1] = unsorted[j-1],unsorted[j] #swap

for i in range(len(unsorted)) :
   print(unsorted[i])   
        
        
  