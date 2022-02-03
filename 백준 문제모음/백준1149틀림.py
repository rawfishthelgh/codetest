import sys
input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
costs=[[1001,1001,1001,0]]
for _ in range(n):
  r,g,b=map(int,input().split())
  costs.append([r,g,b])

print(costs)
buf=0
for i in range(1,n+1):
  mincost=min(costs[i])
  if costs[i].index(mincost)==costs[i-1].index(buf):
    a=sorted(costs[i])
    mincost=a[1]
    print(a[1])
  dp[i]=dp[i-1]+mincost
  buf=mincost

print(dp)