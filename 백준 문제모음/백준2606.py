from collections import deque
#노드의 수
n=int(input())
#간선의 수
m=int(input())
#연결 정보
graph=[[] for i in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()
#방문 정보
visited=[False]*(n+1)

#bfs함수 정의

def bfs(graph,v,visited):
  #바이러스 걸리는 컴퓨터 수
  cnt=0
  queue=deque([v])
  visited[v]=True
  while queue:
    v=queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True
        cnt+=1
  print(cnt)
#bfs 실행
bfs(graph,1,visited)


