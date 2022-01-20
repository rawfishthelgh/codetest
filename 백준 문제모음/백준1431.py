n=int(input())
cnum=[input()for _ in range(n)]

def totalnum(x):
  ans=0
  for i in  x:
    if i.isdigit():
      ans+=int(i)
  return ans
cnum.sort(key=lambda x:(len(x),totalnum(x),x))
for i in cnum:
  print(i)