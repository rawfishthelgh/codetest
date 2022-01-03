n,k = map(int,input().split())
cnt=0
while(True):
  #n이 k로 나눠지는 수(target)가 되기까지 1을 몇 번 빼야 하는지 구하기
  target=(n//k)*k
  cnt += (n-target)
  n= target
  #n이 k보다 작을 때(더 이상 나눌 수 없을 때)반복문 탈출
  if n<k:
    break
  #n이 k보다 작지 않을 때 나누기 수행
  cnt +=1
  n //= k

#마지막으로 남은 수에 대해 1씩 뺀 값 구하기
cnt += (n-1)
print(cnt)