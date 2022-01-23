#국가수 n, 등수를 알고싶은 국가
n,k=map(int,input().split())
nations=[list(map(int,input().split())) for _ in range(n)]

nations.sort(key= lambda x:(-x[1],-x[2],-x[3]))

for i in range(n):
  if nations[i][0]==k:
    index=i

for i in range(n):
  if nations[index][1:]==nations[i][1:]:
    print(i+1)
    break