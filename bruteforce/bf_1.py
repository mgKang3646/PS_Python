
items = []
total = 0 
flag = False
for _ in range(9) :
  items.append(int(input()))

total = sum(items)

for i in range(9) :
  if flag : break
  for j in range(1,9) :
    if i == j : continue
    value = total - (items[i] + items[j])
    if value == 100 : 
      flag = True
      delete1 = items[i]
      delete2 = items[j]
      items.remove(delete1)
      items.remove(delete2)
      break

items.sort()
for item in items :
  print(item)
