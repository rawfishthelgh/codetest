import sys
input=sys.stdin.readline
n=int(input())
#나눌 나머지
m=1000000
#주기
p=15*(m//10)

array=[0,1]


for i in range(2,p):
  array.append(fibo[i-1]+fibo[i-2])
  #N번째 피보나치 수를 M으로 나눈 수로 저장
  fibo[i] %= m

# N번째 피보나치 수를 M으로 나눈 수==N%p 번째 피보나치수를 m으로 나눈 수
# 따라서 테이블에 이미 N번째 피보나치 수를 M으로 나눈 수가 저장돼 있으므로
# n%p번째를 인덱싱하면 값을 얻을 수 있다
print(fibo[n%p])