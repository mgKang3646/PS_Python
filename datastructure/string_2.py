
n = int(input())

for _ in range(n) :
  input_value = input()
  input_list = list(input_value)
  total = 0 
  for value in input_list :
    if value == "(" : total += 1
    elif value == ")" : total -= 1

    if total < 0 : 
      print("NO")
      break
  
  if total > 0 : print("NO")
  elif total == 0 : print("YES")
    