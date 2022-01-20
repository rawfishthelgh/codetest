t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  a.sort(reverse=True)
  b.sort(reverse=True)
  cnt=0
  a_index=0
  b_index=0
  while (a_index < n) and (b_index < m):
    if a[a_index]>b[b_index]:
      cnt+= m-(b_index)
      a_index+=1
    else:
      b_index+=1
  print(cnt)