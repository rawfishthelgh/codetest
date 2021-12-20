from collections import deque
#맵 크기 입력
n,m=map(int,input().split())
#맵 정보 입력
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

#이동할 네 가지 방향 정의(상하좌우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#bfs 소스코드 구현
def bfs(x,y):
  queue = deque()
  queue.append((x,y)) #첫 위치 삽입
  #큐가 빌 때까지 반복
  while queue:
    x,y=queue.popleft()
    #현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #공간 벗어나면 무시
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      #괴물인 경우 무시
      if graph[nx][ny]==0:
        continue
      #해당 노드 처음 방문하는 경우, 즉 1인 경우(이동가능한 경우)에만 최단 거리 기록
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  #가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

print(bfs(0,0))
