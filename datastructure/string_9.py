#BOJ11655

#0-12 : + 13
#13-25 : -13 

import sys
input = sys.stdin.readline

st = list(input().rstrip("\n"))

for char in st :
  if char.isalpha() :
    if char.isupper() :
      if ord(char) - ord("A") < 13 : print(chr(ord(char)+13),end="")
      else : print(chr(ord(char)-13),end="")   
    else :
      if ord(char) - ord("a") < 13 : print(chr(ord(char)+13),end="")
      else : print(chr(ord(char)-13),end="")

  else : 
    print(char,end="")