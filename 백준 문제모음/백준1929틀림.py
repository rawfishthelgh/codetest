import sys
import math
n,m=map(int,input().split())
# 최대길이 m+1 만큼의 배열 선언
array=[True for i in range(m+1)]

#에라토스테네스의 체 이용 소수가 아닌 인덱스는 모두 False로
for i in range(n,int(math.sqrt(m))+1):
    if array[i]==True:
        j=2
        while i*j <=m:
            array[i*j]=False
            j+=1

#True 값인 인덱스만 반환
for i in range(n,m+1):
    if array[i]:
        print(i)