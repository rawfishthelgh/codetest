import sys
import math
sqrt=math.sqrt
input=sys.stdin.readline
#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
#노드의 개수와 간선(union연산)의 개수 입력 받기
n= int(input())
parent=[0]*(n+1)
# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges=[]
result=0
#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i
#좌표정보
loc=[]
for _ in range(n):
  a,b=map(float,input().split())
  loc.append((a,b))

for i in range(n-1):
  for j in range(i+1,n):
    edges.append((sqrt(((loc[i][0]-loc[j][0])**2)+(loc[i][1]-loc[j][1])**2),i,j))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b= edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(round(result,2))