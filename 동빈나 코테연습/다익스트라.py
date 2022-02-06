import sys
input=sys.stdin.readline
#노드의 개수, 간선의 개수
n,m=map(int,input().split())
start=int(input()) #시작점(start)

INF= int(1e9) #10억, 무한 의미
#노드의 연결 정보 리스트 생성
graph=[[] for i in range(n+1)]
#방문 여부 체크하는 리스트 생성
visited=[False]*(n+1)
#최단거리 테이블을 무한으로 초기화해 생성
distance=[INF]*(n+1)

#모든 간선 정보 입력받기
for _ in range(m):
  a,b,c=map(int,input().split())
  #a번노드에서 b로 가는 비용은 c다
  graph[a].append((b,c))

#방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드번호 반환
def get_smallest_node():
  min_value= INF
  index=0 #가장 최단 거리가 짧은 노드 선택
  for i in range(1,n+1):
    #방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
    if distance[i]<min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  #시작 노드에 대해 초기화:0
  distance[start]=0
  visited[start]=True
  #출발 노드로부터 인접한 노드로부터의 거리 갱신
  for j in graph[start]:
    distance[j[0]]=j[1]
  #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    #매번 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
    now=get_smallest_node()
    visited[now]=True
    #꺼내진 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      #시작 노드부터 현재 노드까지 오는 길이에, 현재 노드에서 인접한 노드로 가는 길이를 더함
      cost=distance[now]+j[i]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 길이 갱신
      if cost < distance[j[0]]:
        distance[j[0]]=cost

#다익스트라 알고리즘 수행
dijkstra(start)
#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
  #도달할 수 없으면 무한 출력
  if distance[i]==INF:
    print("INF")
  #도달할 수 있으면 거리 출ㄺ
  else:
    print(distance[i])