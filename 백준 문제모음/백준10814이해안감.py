n=int(input())
members={}
for _ in range(n):
  x,y=input().split()
  x=int(x)
  members[y]=x

age=[]
for i in members.values():
  if i not in age:
    age.append(i)
age.sort()

for i in age:
  for x,y in members.items():
    if y==i:
      print(y,x)