#사람수
n=int(input())
a=list(map(int,input().split()))
a.sort()
time=0
alltime=0

for i in a:
  time += i
  alltime += time

print(alltime)