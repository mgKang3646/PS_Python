
n = int(input())

array = []
for _ in range(n) :
  array.append(list(input().split()))
  
array = sorted(array,key= lambda student : student[1]) 
# student 매개변수를 받아서 studen[1]를 반환해서 key에 넣겠다. 
# 정렬 기준을 1번 인덱스일지 2번 인덱스일지... 람다로 정해서 반환해주어야 한다. 

for student in array :
  print(student[0],end=" ")