import sys
n=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
m=int(input())
nums=list(map(int,sys.stdin.readline().split()))
array.sort()
start=0
end=n-1
result=[]
def binary_search(array,x,start,end):
  cnt=0
  while(start<=end):
    array.sort()
    mid=(start+end)//2
    if array[mid]==x:
      cnt+=1
      array[mid]=10000001 
    elif array[mid]>x:
      end=mid-1
    else:
      start=mid+1
  return cnt

for x in nums:
  a=binary_search(array,x,start,end)
  result.append(a)
for i in result:
  print(i,end=" ")