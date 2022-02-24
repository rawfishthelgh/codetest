import sys
import math
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

def is_prime_number(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True

primenum=[]

for i in a:
  if is_prime_number(i):
    primenum.append(i)

def solution(primenum):
    from math import gcd
    ans=primenum[0]
    for num in primenum:
      ans=(ans*num)//gcd(ans, num)
    return ans
    
print(solution(primenum))    