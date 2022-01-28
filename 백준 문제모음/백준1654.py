import sys
k,n=map(int,sys.stdin.readline().split())
length=[]
for _ in range(k):
  length.append(int(sys.stdin.readline()))
length.sort()
start=0
end=max(length)
result=0

while(start<=end):
  total=0
  mid=(start+end)//2
  for i in length:
    if i>=mid:
      total+=i//mid
  if total>=n:
    result=mid
    start=mid+1
  else: #total<n
    end=mid-1

print(result)