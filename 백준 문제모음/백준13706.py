n=int(input())
start=1
end=n
def binary_search(start,end,n):
  while True:
    mid=(start+end)//2
    if mid**2==n:
      return mid
      break
    elif mid**2>n:
      end=mid-1
    else:
      start=mid+1
  return -1

print(binary_search(start,end,n))