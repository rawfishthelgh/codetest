import sys
import copy
input= sys.stdin.readline

n=int(input())
maxn=2*n-1
num='*'*maxn
mlist=[]
mlist.append(list(num))

for i in range(1,n):
  nownum=copy.deepcopy(mlist[i-1])
  nownum[i-1]=' '
  nownum[-i]=' '
  mlist.append(nownum)
for i in range(n-2,-1,-1):
  nownum=copy.deepcopy(mlist[i])
  mlist.append(nownum)

for i in mlist:
  for j in i:
    print(j,end="")
  print()