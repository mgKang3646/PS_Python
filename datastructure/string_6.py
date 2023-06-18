import sys
input = sys.stdin.readline

alphas = [0]*26
st = list(input().rstrip())

for char in st :
  alphas[ord(char)-ord("a")] +=1

for alpha in alphas :
  print(alpha,end=" ")