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

now=100000

for i in arrp:
  for j in arrm:
    temp=abs(i+j)
    if now>temp:
      now=temp
      result=[i,j]
      result.sort()
      
print(result[0],result[1])