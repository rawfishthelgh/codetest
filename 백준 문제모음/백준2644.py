from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())

visited=[False]*(n+1)
graph=[[] for i in range(n+1)]

for i in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(start,end):
  cnt=0
  queue=deque([[start,cnt]])
  while queue:
    v=queue.popleft()
    now=v[0]
    cnt=v[1]
    if now==end:
      return cnt
    cnt+=1
    for i in graph[now]:
      if not visited[i]:
        visited[i]=True
        queue.append([i,cnt])
  return -1

print(bfs(a,b))