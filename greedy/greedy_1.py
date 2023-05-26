n,m = map(int,input().split())
max_result = 0

for _ in range(n) :
  line = list(map(int,input().split()))
  min_value = min(line)
  max_result = max(max_result,min_value)
 
print(max_result)