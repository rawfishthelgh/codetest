import sys
input = sys.stdin.readline


n,d,k,c=map(int,input().split())
arr=[int(input().rstrip()) for _ in range(n)]
start=0
end=0
result=0
#start 점을 계속 바꿔가며 시작점에서 k개를 연속으로 먹으면서 비교
while start<n:
  end=(start+k)
  #쿠폰 초밥을 더 먹을 수 있는지 여부 판단
  add=True
  # set 자료형을 이용해서 범위 내 초밥의 종류를 중복 없이 담음
  numset=set()
  #배열이 원형이므로 n으로 나눈 나머지 구하면 n+i을 i로 간주 가능
  for i in range(start,end):
    i %= n
    #초밥의 종류 담아줌
    numset.add(arr[i])
    #이미 범위 안에 있는 초밥이면 쿠폰 초밥종류 못 더함
    if arr[i]==c:
      add=False
  #결국 범위 내 초밥의 종류를 넘버셋의 길이를 통해 구할 수 있음
  cnt=len(numset)
  # 범위 내에 쿠폰이 없으면 하나 더 먹을 수 있음
  if add==True:
    cnt+=1
  #최댓값 계속 갱신
  result=max(result,cnt)
  start+=1

print(result)
