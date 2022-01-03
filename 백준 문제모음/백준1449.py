n,l=map(int,input().split())
spots=list(map(int,input().split()))
#리스트를 정렬한다

spots.sort()

start=0 #현재 위치
count=0

for spot in spots:
  #배열에서 현재 위치보다 작은 값은 전부 무시가능
  if start<spot:
    #현재 위치를 해당 배열+길이-1로 변경
    start += spot+l-1
    #테이프 증가
    count+=1
print(count)