n=int(input())
array=list(map(int,input().split()))
m=int(input())
nums=list(map(int,input().split()))
array.sort()
start=0
end=n-1
result=[]
def binary_search(array,x,start,end):
  while(start<=end):
    mid=(start+end)//2
    if array[mid]==x:
      return True
    elif array[mid]>x:
      end=mid-1
    else:
      start=mid+1
  return False

for x in nums:
  if binary_search(array,x,start,end)==True:
    result.append(1)
  else:
    result.append(0)

for i in result:
  print(i,end=" ")