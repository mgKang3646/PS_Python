#BOJ11656 

import sys 
input =sys.stdin.readline

suffix= []
word = list(input().rstrip())

for i in range(len(word)) :
  suffix.append("".join(word[i:]))

suffix.sort()

for st in suffix :
  print(st)