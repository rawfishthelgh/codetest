n=int(input())
cnum=[input() for _ in range(n)]
def checknum(x):
  total=0
  for i in x:
    if i.isdigit()==True:
      total+=int(i)
  return total
cnum.sort(key=lambda x:(len(x),checknum(x),x))
for i in cnum:
  print(i)