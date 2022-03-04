import sys
from collections import deque
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
  list_=list(input())
  list_.pop()
  for i in range(len(list_)):
    list_[i]=int(list_[i])
  graph.append(list_)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# #dfs풀이
# def dfs(x,y):
#   if 0<=x<n and 0<=y<n and graph[x][y]==1:
#     global cnt
#     cnt+=1
#     graph[x][y]=0
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if 0>nx or nx>n or 0>ny or ny>n:
#         continue
#       dfs(nx,ny)
#     return True
#   return False
      
# cnt=0
# result=[]

# for i in range(n):
#   for j in range(n):
#     if dfs(i, j)==True:
#       result.append(cnt)
#       cnt=0
# result.sort()
# print(len(result))
# for i in result:
#   print(i)
      
# #bfs풀이
# def bfs(x,y):
#   queue=deque()
#   queue.append((x,y))
#   graph[x][y]=0
#   cnt=1
#   while queue:
#     x,y=queue.popleft()
#     for i in range(4):
#       nx=x+dx[i]
#       ny=y+dy[i]
#       if 0>nx or nx>=n or 0 >ny or ny>=n:
#         continue
#       if graph[nx][ny]==1:
#         graph[nx][ny]=0
#         queue.append((nx,ny))
#         cnt+=1
#   return cnt
  
# result=[]

# for i in range(n):
#   for j in range(n):
#     if graph[i][j]==1:
#       result.append(bfs(i,j))
# result.sort()
# print(len(result))
# for i in result:
#   print(i)
