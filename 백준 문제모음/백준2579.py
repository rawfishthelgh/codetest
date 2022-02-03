import sys
input=sys.stdin.readline

#n계단까지 벌 수 있는 최대수익을 저장
d=[]
floorlist=[]

n=int(input())
for _ in range(n):
  floorlist.append(int(input()))

for i in range(n):
  if i==0:
    d.append(floorlist[0])
  elif i==1:
    d.append(max(floorlist[0]+floorlist[1],floorlist[1]))
  elif i==2:
    d.append(max(floorlist[0]+floorlist[2],floorlist[1]+floorlist[2]))
  else:
    d.append(max(d[i-2]+floorlist[i],d[i-3]+floorlist[i]+floorlist[i-1]))

print(d.pop())