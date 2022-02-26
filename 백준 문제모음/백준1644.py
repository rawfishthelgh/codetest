import sys
import math
input = sys.stdin.readline

n=int(input())
array=[True for i in range(n+1)]
data=[]

for i in range(2,int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j <=n:
            array[i*j]=False
            j+=1

for i in range(2,n+1):
    if array[i]:
        data.append(i)

count=0
interval_sum=0
end=0
datalen=len(data)

for start in range(datalen):
    while interval_sum < n and end < datalen:
        interval_sum += data[end]
        end += 1
    
    if interval_sum ==n:
        count += 1
    interval_sum -= data[start]

print(count)


