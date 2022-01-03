n=int(input())
scared=list(map(int,input().split()))

scared.sort()

cnt=0  #총 그룹수
groupnum=0 #그룹 포함된 모험가 수
for i in range(n):
  groupnum += 1
  if scared[i]<=groupnum:
    cnt+=1
    groupnum=0
print(cnt)
