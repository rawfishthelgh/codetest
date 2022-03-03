import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]
  graph[x][y]=0
  for i in range(8):
    nx = x +dx[i]
    ny = y+dy[i]
    if 0<=nx<m and 0<=ny<n and graph[nx][ny]==1:
      dfs(nx,ny)

while True:
  n,m=map(int,input().split())
  if n==0 and m==0:
    break
  graph=[]
  for _ in range(m):
    graph.append(list(map(int,input().split())))
  cnt=0
  for i in range(m):
    for j in range(n):
      if graph[i][j]==True:
        dfs(i,j)
        cnt+=1
  print(cnt)
    