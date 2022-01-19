n=int(input())
members=[]
for _ in range(n):
  x,y=input().split()
  x=int(x)
  members.append([x,y])
members.sort(key=lambda x:x[0])
for i in range(n):
  print(members[i][0],members[i][1])