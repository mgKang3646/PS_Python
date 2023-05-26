

def sequenceSearch(size, target, array) :
  for i in range(size) :
    if target == array[i] :
      return array[i]
  
info = input.split()
size = info[0]
target = info[1]

array = input.split()

result = sequenceSearch(size,target,array)

print(result)
