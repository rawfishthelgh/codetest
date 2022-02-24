import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]*(n+m)

start=0
end=0
now=0


while start<n or end<m:
  #end값이 m보다 같거나 크면 더이상 집어넣을 b 값이 없으므로 남은 a 밀어넣음
  if end>=m or (start<n and a[start]<=b[end]):
    c[now]=a[start]
    start+=1
  else:
    c[now]=b[end]
    end+=1
  now+=1

for i in c:
    print(i, end=' ')
