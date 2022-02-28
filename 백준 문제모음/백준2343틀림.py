n,m=map(int,input().split())
length=list(map(int,input().split()))
length.sort()
start=1
end=sum(length)
result=0
while start<=end:
  mid=(start+end)//2
  lengthsum=0
  cnt=1
  for i in length:
    if (mid-lengthsum)<i:
      cnt+=1
      lengthsum=0
    lengthsum+=i
  if cnt<=m:
    result=mid
    end=mid-1
  else:
    start=mid+1
print(result)