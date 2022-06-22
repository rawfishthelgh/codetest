import sys
input= sys.stdin.readline

clist=list(map(int,input().split()))
olist=[1,1,2,2,2,8]
newlist=[]
for i in range(6):
  num=olist[i]-clist[i]
  newlist.append(num)

for i in newlist:
  print(i,end=" ")