import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
  buff=list(map(int,input().split()))
  arr.append(buff)

visited=[]
for _ in range(n):
  visited.append([0 for _ in range(n)])

def dfs(x,y,arr):
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False
  k=arr[x][y]
  if visited[x][y]==0:
    visited[x][y]=1
    dfs(x+k,y,arr)
    dfs(x,y+k,arr)
    return True
    
dfs(0,0,arr)
if visited[n-1][n-1]==1:
  print("HaruHaru")
else:
  print("Hing")
  