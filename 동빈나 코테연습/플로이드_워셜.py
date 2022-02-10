import sys
input=sys.stdin.readline
INF=int(1e9) #무한

#노드 n 간선 m
n=int(input())
m=int(input())

#2차원 리스트(그래프)만들고 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
        graph[a][b]=0

#각 간선 정보 입력 받아 값 초기화
for _ in range(m):
  #a에서 b로 가는 비용 c
  a,b,c=map(int,input().split())
  graph[a][b]=c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#수행된 결과 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    #도달할 수 없으면 무한 출력
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b],end=" ")
  print()