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

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

cycle=False #사이클 발생 여부

for i in range(e):
    a,b=map(int,intpue().split())
    #사이클이 발생한 경우 종료(두 원소가 같은 집합에 속함)
    if find_parent(parent,a) == find_parent(parent,b):
        cycle=True
        break
    #사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생하지 않음")