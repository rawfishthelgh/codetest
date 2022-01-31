import sys
input=sys.stdin.readline
n=int(input())
array=[3,5]
d=[5001]*(n+1)

d[0]=0
for i in range(len(array)):
  for j in range(array[i],n+1):
    if d[j-array[i]]!=5001:
      d[j]=min(d[j],d[j-array[i]]+1)

if d[n]==5001:
  print(-1)
else:
  print(d[n])