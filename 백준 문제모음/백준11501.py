import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
  n=int(input())
  arr=list(map(int,input().split()))
  result=0
  maxnum=0
  for i in range(len(arr)-1,-1,-1):
    now=arr[i]
    if now>maxnum:
      maxnum=now
    else:
      result+=(maxnum-now)
    
  # for i in range(n-1):
  #   now=arr[i]
  #   maxnum=max(arr[i:])
  #   if now==maxnum:
  #     continue
  #   result+=(maxnum-now)
  
  print(result)