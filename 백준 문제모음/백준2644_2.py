from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[]for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(a,b):
  queue=deque([a])
  visited[a]=True
  while queue:
    v=queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i]=visited[v]+1
        queue.append(i)
  return visited[b]

print(bfs(a,b)-1)