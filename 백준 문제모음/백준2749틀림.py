import sys
input=sys.stdin.readline
n=int(input())
array=[]

for i in range(n+1):
  if i==0:
    array.append(i)
  elif i==1:
    array.append(i)
  else:
    array.append(array[i-1]+array[i-2])

print(array.pop()%1000000)