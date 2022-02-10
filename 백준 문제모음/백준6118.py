import sys
import heapq
input=sys.stdin.readline
#노드의 개수, 간선의 개수
n,m=map(int,input().split())

INF= sys.maxsize #무한
#노드의 연결 정보 리스트 생성
graph=[[] for _ in range(n+1)]

#최단거리 테이블을 무한으로 초기화해 생성
distance=[INF]*(n+1)

#모든 간선 정보 입력받기
for _ in range(m):
  a,b=map(int,input().split())
  #a번노드에서 b로 가는 비용은 1이다
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q=[]
  #시작 노드에 대해 초기화:0 큐에 삽입
  distance[0]=0
  distance[start]=0
  heapq.heappush(q,(0,start))
  while q: #큐가 비어있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 거리와 노드 꺼내기
    dist,now=heapq.heappop(q)
    #현재 꺼낸 값이 갱신 전보다 작으면 무시
    if distance[now]<dist:
      continue
    #현재 노드가 이미 처리된 적이 있는 노드면 무시
    #현재 꺼낸 거리 값이 테이블에 기록된 거리보다 크면 이미 처리가 된 것임
    #꺼내진 현재 노드와 연결된 다른 노드를 확인
    #v는 인접 노드, w는 인접 노드까지의 거리
    for v,w in graph[now]:
      #시작 노드부터 현재 노드까지 오는 길이에, 현재 노드에서 인접한 노드로 가는 길이를 더함
      cost=dist+w#dist는 현재 확인하는 노드까지의 거리값, w은 인접 노드까지의 거리 값을 의미
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 길이 갱신
      #즉 cost값이 현재 그 노드에 대한 거리 정보보다 짦으면
      if cost < distance[v]:
        distance[v]=cost
        #값이 갱신될때마다 우선순위 큐에 해당 정보 반영
        heapq.heappush(q,(cost,v))

#다익스트라 알고리즘 수행
dijkstra(1)
#모든 노드로 가기 위한 최단 거리를 출력
maxindex=distance.index(max(distance))
maxfar=distance[maxindex]
maxcount=distance.count(maxfar)

print(maxindex,maxfar,maxcount)