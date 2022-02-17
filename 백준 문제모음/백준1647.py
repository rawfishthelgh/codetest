import sys
input=sys.stdin.readline
#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])#부모 테이블 값 바로 갱신
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    #둘 중 더 큰 쪽이 다른 쪽을 부모로 설정
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union연산)의 개수 입력 받기
v,e = map(int,input().split())
parent=[0]*(v+1) #1부터 v까지 모든 노드에 대해 부모 정보를 담을 수 있도록 리스트 만듦

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges=[]
result=0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()
#포함된 간선 길이
line=[]
#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b= edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        line.append(cost)

print(result-line.pop())