import sys
input=sys.stdin.readline
n=int(input())
start=0
end=n-1
cnt=0
numlist=list(map(int,input().split()))
numlist.sort()
x=int(input())

while start<end:
  intervalsum=numlist[start]+numlist[end]
  if intervalsum==x:
    cnt+=1
    start+=1
  elif intervalsum>x:
    end-=1
  elif intervalsum<x:
    start+=1

print(cnt)