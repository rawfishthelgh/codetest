x,y=map(int,input().split())

start=0
end=x
z=(y*100)//x
result=0
while start<=end:
  mid=(start+end)//2
  z2=((y+mid)*100)//(x+mid)
  if z!=z2:
    result=mid
    end=mid-1
  else:
    start=mid+1
  
if result==0:
  print('-1')
else:
  print(result)