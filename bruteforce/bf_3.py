

e,s,m = map(int,input().split())
value = 0

while True :
  value += 1
  
  e_tmp = value%15
  s_tmp = value%28
  m_tmp = value%19

  if e_tmp == 0 : e_tmp = 15
  if s_tmp == 0 : s_tmp = 28
  if m_tmp == 0 : m_tmp = 19
    
  if e_tmp == e and s_tmp == s and m_tmp == m : break


print(value)
    
  