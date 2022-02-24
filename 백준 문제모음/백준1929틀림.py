import sys
import math
n,m=map(int,input().split())

array=[True for i in range(m+1)]

for i in range(n,int(math.sqrt(m))+1):
    if array[i]==True:
        j=2
        while i*j <=m:
            array[i*j]=False
            j+=1

for i in range(n,m+1):
    if array[i]:
        print(i)