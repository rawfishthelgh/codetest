import sys
import heapq

n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]

h=[]

def heapsort(arr,k):
  for i in range(len(arr)):
    for value in arr[i]:
      heapq.heappush(h, (-value,value))

  kth_max=None

  for _ in range(k):
    kth_max=heapq.heappop(h)[1]
    
  return kth_max

print(heapsort(arr,n))