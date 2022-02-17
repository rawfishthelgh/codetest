import sys
input=sys.stdin.readline
#특정 원소가 속한 집합의 루트번호 찾기
def find_parent(parent,x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x]!= x:
        return find_parent(parent,parent[x])
    return x

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

#union 연산을 각각 수행
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력하기
print("각 원소가 속한 집합:", end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

#부모 테이블 내용 출력하기
print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')