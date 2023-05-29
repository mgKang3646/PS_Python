n = int(input())
data = []
for _ in range(n) :
  data.append(int(input()))

data = sorted(data,reverse=True)

for value in data :
  print(value, end=" ")