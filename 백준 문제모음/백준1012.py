import sys
sys.setrecursionlimit(10**6)
#테스트 케이스
t=int(input())
for _ in range(t):
  #가로길이 m, 세로길이 n, 배추의 수 k
  m,n,k=map(int,input().split())
  #배추 위치정보
  graph=[]
  for i in range(m):
    v=[0]*n
    graph.append(v)
  for i in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1


  #dfs 정의
  def dfs(x,y):
    if x<=-1 or x>=m or y<=-1 or y>=n:
      return False
    if graph[x][y]==1:
      graph[x][y]=0
      dfs(x-1,y)
      dfs(x,y-1)
      dfs(x+1,y)
      dfs(x,y+1)
      return True
    return False

  #모든 배추에 대해 지렁이 수 찾기
  cnt=0
  for i in range(m):
    for j in range(n):
      #현재 위치에서 dfs 수행
      if dfs(i,j)==True:
        cnt+=1
  print(cnt)