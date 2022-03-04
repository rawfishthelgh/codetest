import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
  list_=list(map(int,input().split()))
  arr.append(list_)


for i in range(1,n):
  for j in range(len(arr[i])):
    if j!=0 and j!=(len(arr[i])-1):
      arr[i][j]=max(arr[i-1][j],arr[i-1][j-1])+arr[i][j]
    elif j==0:
      arr[i][j]=arr[i-1][j]+arr[i][j]
    elif j==(len(arr[i])-1):
      arr[i][j]=arr[i-1][j-1]+arr[i][j]

print(max(arr[n-1]))