#아이스크림 얼려먹기
#dfs 메소드 선언해서 특정 노드방문하고 연결된 노드도 방문
def dfs(x,y):
  #주어진 범위 벗어나면 종료
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  #현재 노드 방문하지 않았다면
  if graph[x][y]==0:
    #해당 노드 방문 처리
    graph[x][y]=1
    #상,하,좌,우 위치들 재귀적 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

#행렬 정보 입력받기
n,m=map(int,input().split())
#2차원 리스트 맵 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))
#모든 노드에 대하여 음료수 채우기
result=0 #아이스크림 개수
for i in range(n):
  for j in range(m):
    #현재 위치에서 dfs 수행
    if dfs(i,j)==True: #방문처리가 되었다면
      result+=1 #1씩 증가

print(result)