import sys
input=sys.stdin.readline
n=int(input())
numlist=list(map(int,input().split()))
numlist.sort()
x=int(input())
cnt=0
end=n-1

for start in range(n):
  while start<end:
    intervalsum=numlist[start]+numlist[end]
    if intervalsum==x:
      cnt+=1
      break
    elif intervalsum>x:
      end-=1
    elif intervalsum<x:
      break

print(cnt)