n=input()
alp=[]
value=0
for i in n:
  if i.isalpha():
    alp.append(i)
  else:
    value += int(i)

alp.sort()
if value!=0:
  alp.append(str(value))
print(''.join(alp))
