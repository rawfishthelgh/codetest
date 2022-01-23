n,k=map(int,input().split())
nations=[list(map(int,input().split())) for _ in range(n)]

nations.sort(key= lambda x:(-x[1],-x[2],-x[3]))

cnt=0
for i in range(n):
  cnt+=1
  if nations[i][0]==k:
    if i==0:
      print(cnt)
      break
    if nations[i-1][1:]==nations[i][1:]:
      cnt-=1
      print(cnt)
      break
    print(cnt)
    break