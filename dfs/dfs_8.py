
# 연속된 3잔을 모두 마실수 없다. 
# 많은 양의 포도주를 맛보고 싶다. ( 개 X )
# DFS 마시는 경우, 마시지 않는 경우 ( 연속 카운트 )
# 시간초과 발생
# 2^10,000 번 연산하게 되어 시간초과 발생
# boj2156 포도주 시식

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

answer = 0
n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))
  
def dfs(arr,sum,idx,sequence_count) :

    global answer

    #탈출조건
    if idx == n :
        answer = max(answer,sum)
        return
    
    # 와인을 마시는 경우
    if(sequence_count < 2) : dfs(arr,sum+arr[idx],idx+1,sequence_count+1)

    # 와인을 마시지 않는 경우
    dfs(arr,sum,idx+1,0)


dfs(arr,0,0,0)
print(answer)
    