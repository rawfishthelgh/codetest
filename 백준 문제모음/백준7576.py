from collections import deque


m,n=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]

dx,dy=[-1,1,0,0],[0,0,-1,1]
ans=0

def bfs(m,n):
  queue=deque([])
  for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx,ny=dx[i]+x,dy[i]+y
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        queue.append([nx,ny])

bfs(m,n)

for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))

print(ans-1)