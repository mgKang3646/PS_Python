n = int(input())
room = list(map(int,input().split()))

room_info = []
for i in range(n) :
  room_info += [[i,room[i]]]

# 열을 기준으로 내림차순 정렬
room_info.sort(key=lambda x:-x[1])

result_index = []
result = []
for index, value in room_info :
  if index-1 not in result_index and index+1 not in result_index : 
    result_index += [index]
    result += [value]

print(sum(result))