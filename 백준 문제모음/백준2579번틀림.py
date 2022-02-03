import sys
input=sys.stdin.readline
n=int(input())

#n계단까지 벌 수 있는 최대수익을 저장
d=[0]*301
floorlist=[0]
for _ in range(n):
  x=int(input())
  floorlist.append(x)

# print(floorlist)
cnt=0
for i in range(1,n):
  x=floorlist[i]
  d[i]=max(d[i-1]+x,d[i-2]+x)
  if i==1:
    continue
  if cnt==1:
    d[i]=d[i-2]+x
    cnt=0
  if d[i]==d[i-1]+x:
    cnt+=1
  


# print(d)


if cnt==1:
  print(d[n-2]+floorlist[n])
else:
  print(d[n-1]+floorlist[n])