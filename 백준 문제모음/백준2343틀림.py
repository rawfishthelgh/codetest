n,m=map(int,input().split())
length=list(map(int,input().split()))
length.sort()
start=1
end=sum(length)
result=0
while start<=end:
  mid=(start+end)//2
  print("mid:",mid)
  lengthsum=0
  cnt=1
  for i in length:
    print("i:",i)
    if (mid-lengthsum)<i:
      cnt+=1
      lengthsum=0
    lengthsum+=i
    print("lengthsum:",lengthsum)
  print("cnt:", cnt)
  if cnt<=m:
    result=mid
    end=mid-1
  else:
    start=mid+1
print(result)