import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

#소수인지 확인하는 함수
def is_prime_number(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
#소수담을 리스트
primenum=[]
#소수면 리스트에 담음
for i in a:
  if is_prime_number(i):
    primenum.append(i)
#최소공배수 구하는 함수 인자로 배열을 받음
def solution(primenum):
    #최대공약수 라이브러리
    from math import gcd
    ans=primenum[0]
    # 두 수를 곱한 것을 두 수의 최대공약수로 나누면 최소공배수
    for num in primenum:
      ans=(ans*num)//gcd(ans, num)
    return ans

#솔루션 함수 이용 최소공배수 도출
print(solution(primenum))    