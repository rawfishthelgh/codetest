n=int(input())
#현재위치
x,y=1,1
plans=list(map(str,input().split()))

#L,R,U,D 이동방향(방향벡터 설정)
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

#이동 계획 하나씩 확인
for plan in plans:
  #이동 후 좌표 구함
  for i in range(len(move_types)):
     if plan==move_types[i]:
       nx=x+dx[i]
       ny=y+dy[i]
  #공간 벗어나는 경우 무시
  if nx<1 or nx>n or ny<1 or ny>n:
    continue
  #이동 수행
  x,y=nx,ny

print(x,y) 