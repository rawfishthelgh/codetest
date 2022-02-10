import sys
import heapq
input=sys.stdin.readline
#노드의 개수, 간선의 개수
n,m,start=map(int,input().split())

INF= int(1e9) #10억, 무한 의미
#노드의 연결 정보 리스트 생성
graph=[[] for i in range(n+1)]
#최단거리 테이블을 무한으로 초기화해 생성
distance=[INF]*(n+1)

#모든 간선 정보 입력받기
for i in range(m):
  a,b,c=map(int,input().split())
  #a번노드에서 b로 가는 비용은 c다
  graph[a].append((b,c))

def dijkstra(start,distance):
  q=[]
  #시작 노드에 대해 초기화:0 큐에 삽입
  distance[start]=0
  heapq.heappush(q,(0,start))
  while q: #큐가 비어있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 거리와 노드 꺼내기
    dist,now=heapq.heappop(q)
    #현재 노드가 이미 처리된 적이 있는 노드면 무시
    #현재 꺼낸 값이 갱신 전보다 작으면 무시
    if distance[now]<dist:
      continue
    #현재 꺼낸 거리 값이 테이블에 기록된 거리보다 크면 이미 처리가 된 것임
    #꺼내진 현재 노드와 연결된 다른 노드를 확인
    for i in graph[now]:
      #시작 노드부터 현재 노드까지 오는 길이에, 현재 노드에서 인접한 노드로 가는 길이를 더함
      cost=dist+i[1]#dist는 현재 확인하는 노드까지의 거리값, i[1]은 인접 노드까지의 거리 값을 의미
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 길이 갱신
      #즉 cost값이 현재 그 노드에 대한 거리 정보보다 짦으면
      if cost < distance[i[0]]:
        distance[i[0]]=cost
        #값이 갱신될때마다 우선순위 큐에 해당 정보 반영
        heapq.heappush(q,(cost,i[0]))

#다익스트라 알고리즘 수행
dijkstra(start,distance)

cnt=0
for i in range(1,n+1):
  m=[INF]*(n+1)
  dijkstra(i,m)
  total=distance[i]+m[2]
  cnt=max(cnt,total)
print(cnt)