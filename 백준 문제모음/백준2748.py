import sys
input=sys.stdin.readline
n=int(input())
array=[0]*91
def fibo(n):
  if n==0:
    return 0
  if n==1:
    return 1
  if array[n]!=0:
    return array[n]
  array[n]=fibo(n-1)+fibo(n-2)
  return array[n]

print(fibo(n))