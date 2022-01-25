n,m=map(int,input().split())
height=list(map(int,input().split()))

height.sort()

#시작점 끝점 설정
result=0
start=0
end=max(height)

while (start<=end):
  total=0
  #mid는 절단기의 높이
  mid=(start+end)//2
  for x in height:
    #나무 길이가 절단기 높이보다 크면
    if x>mid:
      #나무를 절단기로 자른 값 더해줌
      total += x-mid
  #나무 길이가 부족할 경우 절단기 길이를 줄임
  if total < m:
    end = mid-1
  #나무 길이가 충분한 경우 절단기 길이를 높임
  else:
    #최대한 덜 잘랐을 때가 정답, result에 기록 
    result=mid
    start=mid+1

print(result)



