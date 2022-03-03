import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
arrp=[]
arrm=[]
for i in arr:
  if i<0:
    arrm.append(i)
  else:
    arrp.append(i)
    

def binary(start,end): 
  now=1000000000
  while start<len(arrm)<end<n:
    mid=(start+end)//2
    temp=abs(arr[start]+arr[end])
    if temp<now:
      now=temp
      start+=1
    else:
      end+=1
  return [arr[start-1],arr[end-1]]
      
start=0
end=n-1
      
for i in (binary(start, end)):
  print(i,end=" ")