import sys
input=sys.stdin.readline
n=int(input())
costs=[]
for _ in range(n):
  r,g,b=map(int,input().split())
  costs.append([r,g,b])
#같은 인덱스가 아닌 것 중 더 비용이 적은 값을 더해나감
for i in range(1,n):
  costs[i][0]=min(costs[i-1][1],costs[i-1][2])+costs[i][0]
  costs[i][1]=min(costs[i-1][0],costs[i-1][2])+costs[i][1]
  costs[i][2]=min(costs[i-1][0],costs[i-1][1])+costs[i][2]

print(costs)
print(min(costs[n-1]))