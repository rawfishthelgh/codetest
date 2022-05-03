import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
  buff=list(map(int,input().split()))
  arr.append(buff)

visited=[]
for _ in range(n):
  visited.append([0 for _ in range(n)])

def bfs(x,y,arr):
  queue= deque()
  queue.append((x,y))

  while queue:
    x,y=queue.popleft()
    visited[x][y]=1
    k=arr[x][y]
    dx=[k,0]
    dy=[0,k]
    for i in range(2):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if visited[nx][ny]==0:
        visited[nx][ny]=1
        queue.append((nx,ny))

bfs(0,0,arr)

if visited[n-1][n-1]==1:
  print("HaruHaru")
else:
  print("Hing")
  