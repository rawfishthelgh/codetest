n,m=map(int,input().split())
length=list(map(int,input().split()))
#블루레이가 최소 전체 강의중 가장 큰 값이 되어야 블루레이에 모든 레슨을 담음
start=max(length)
#블루레이가 모든 레슨의 합이면 블루레이 하나의 모든 레슨 담을 수 있음
end=sum(length)
while start<=end:
  mid=(start+end)//2
  # print("mid:",mid)
  lengthsum=0
  cnt=0
  for i in length:
    # print("i:",i)
    if (mid-lengthsum)<i:
      cnt+=1
      lengthsum=0
    lengthsum+=i
  #루프가 끝나고 남은 lengthsum 값이 존재하면 cnt에 1 더함
  else:
    if lengthsum:
      cnt+=1
  #   print("lengthsum:",lengthsum)
  # print("cnt:", cnt)
  if cnt<=m:
    end=mid-1
  elif cnt>m:
    start=mid+1

#가능한 크기 중 "최소 크기"가 답이므로 최종 start 값 출력
print(start)