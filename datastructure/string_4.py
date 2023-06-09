
import sys
input = sys.stdin.readline

st = list(input().rstrip())

i = 0 
while i < len(st):
  if st[i] == "<" : #태그를 만나는 경우
    while st[i] != ">" : 
      i += 1
    i += 1 

  elif st[i].isalnum() : #문자열을 만나는 경우
    #구간탐색
    start = i 
    while i<len(st) and st[i] != " " and st[i] != "<" :
      i += 1
    #문자열 뒤집기
    tmp = st[start:i]
    tmp.reverse()
    st[start:i] = tmp

  else : i += 1 # 공백을 만나는 경우

#출력
print("".join(st)[:])
    


