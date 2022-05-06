import math
import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
cntarr={}
arr=[]
for _ in range(n):
  k=int(input())
  arr.append(k)
  if k not in cntarr:
    cntarr[k]=1
  else:
    cntarr[k]+=1
arr.sort()

#1. 산술평균
avr1=round(sum(arr)/n)
#2. 중앙값
mid=n//2
avr2=arr[mid]
#3. 최빈값
avr3=0

cntarr=list(cntarr.items())
cntarr.sort(key=lambda x : (-x[1], x[0]))
# print(cntarr)
maxcnt=cntarr[0][1]

if len(cntarr)==1:
  avr3=cntarr[0][0]
else:
  if cntarr[0][1]==cntarr[1][1]:
    avr3=cntarr[1][0]
  else:
    avr3=cntarr[0][0]
#4. 범위
if len(arr)==1:
  avr4=0
else:
  avr4=arr[n-1]-arr[0]
  
#출력
print(avr1)
print(avr2)
print(avr3)
print(avr4)