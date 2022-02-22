import sys
input = sys.stdin.readline
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])#부모 테이블 값 바로 갱신
  return parent[x]
  
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  #둘 중 더 큰 쪽이 다른 쪽을 부모로 설정
  if a<b:
      parent[b] = a
  else:
      parent[a] = b

while True:
  #노드의 개수와 간선(union연산)의 개수 입력 받기
  v,e = map(int,input().split())
  if v==0 and e==0:
    break
  # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
  edges=[]
  total=0
  result=0
  #부모 테이블상에서, 부모를 자기 자신으로 초기화
  parent = [i for i in range(v)]
  #모든 간선에 대한 정보를 입력 받기
  for _ in range(e):
    a,b,cost=map(int,input().split())
    total+=cost
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))
  
  #간선을 비용순으로 정렬
  edges.sort()
  
  #간선을 하나씩 확인하며
  for edge in edges:
    cost,a,b= edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
      union_parent(parent,a,b)
      result += cost
        
  print(total-result)