
import sys
input = sys.stdin.readline

def print_count(st) :
  lower,upper,decimal,blank = 0,0,0,0
  
  for char in st :
    if char == " " : blank += 1
    elif char.isdecimal() : decimal += 1
    else : 
      if char.isupper() : upper += 1
      else : lower += 1
  
  print(lower,upper,decimal,blank)

while True :
  st = input().rstrip('\n')
  if not st : break
  print_count(st)

