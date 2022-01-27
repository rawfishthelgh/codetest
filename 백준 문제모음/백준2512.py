n=int(input())
requests=list(map(int,input().split()))
m=int(input())
requests.sort()

start=0
end=max(requests)
result=0

while(start<=end):
  total=0
  mid=(start+end)//2
  for i in requests:    
    if i>mid:
      total += mid
    else:
      total += i
  if total<=m:
    result=mid
    start=mid+1
  else:
    end=mid-1

print(result)