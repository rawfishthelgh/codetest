from collections import deque

#노드의 개수와 간선(union연산)의 개수 입력 받기
v,e = map(int,input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
#최종 학기수를 담는 리스트
time = [0 for i in range(v + 1)]
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b) #정점 A에서 B로 이동 가능
    #진입 차수를 1 증가
    indegree[b] += 1

#위상 정렬 함수
def toplogy_sort():
    q=deque() #큐 기능을 위한 덱 라이브러리 사용
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입, 진입차수가 초기에 0이면 학기수 값은 1로 고정
    for i in range(1,v+1):
        if indegree[i]==0:
            time[i]=1
            q.append((i,1))
    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기, 학기 수 까지 꺼내줌
        now,cnt = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                q.append((i,(cnt+1)))
                time[i]=cnt+1

toplogy_sort()

for i in range(1,len(time)):
  print(time[i],end=" ")