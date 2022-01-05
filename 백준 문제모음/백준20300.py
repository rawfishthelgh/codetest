import sys
n=int(sys.stdin.readline())
t=list(map(int,sys.stdin.readline().split()))
t.sort()
maxlost=0
if len(t)%2==0:
  for i in range(len(t)//2):
    a=t[i]+t[-1-i]
    if maxlost<a:
      maxlost=a
else:
  maxlost=t.pop(-1)
  for i in range(len(t)//2):
    a=t[i]+t[-1-i]
    if maxlost<a:
      maxlost=a
print(maxlost)