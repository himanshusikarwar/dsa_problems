def prt(n):
  if n == 0:
    return
  print(n, end = ' ') 
  prt(n-1)
  print(n, end = ' ') 
  return 

