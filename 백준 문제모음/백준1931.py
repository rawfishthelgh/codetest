#회의 개수
n=int(input())
timelist=[]
for i in range(n):
  time=list(map(int,input().split()))
  timelist.append(time)

timelist.sort(key=lambda x: (x[1],x[0]))

cnt=1
end_time=timelist[0][1]

for i in range(1,n):
  if timelist[i][0]>=end_time:
    cnt+=1
    end_time=timelist[i][1]
    
print(cnt)