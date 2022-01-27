import sys
k,n=map(int,sys.stdin.readline().split())
length=[]
for _ in range(k):
  length.append(int(sys.stdin.readline()))
length.sort()
start=0
end=max(length)
result=0

def binary_search(length,n,start,end):
  if start>end:
    return None
  total=0
  mid=(start+end)//2
  for i in length:
    if i>=mid:
      total+=i//mid
  if total==n:
    result=mid
    return result
  elif total>n:
    result=mid
    return binary_search(length,n,mid+1,end)
  else:
    return binary_search(length,n,start,mid-1)
  return result

print(binary_search(length,n,start,end))