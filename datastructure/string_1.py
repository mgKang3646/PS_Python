import sys
input = sys.stdin.readline

n = int(input())

def reverse_line(line) :
  for i in range(len(line)) :
    line[i] = ''.join(reversed(line[i]))
  return line

def print_line(line) :
  print()
  for value in line :
    print(value,end=" ")

for _ in range(n) :
  line = input().split()
  line = reverse_line(line)
  print_line(line)
  



