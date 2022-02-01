import sys
input=sys.stdin.readline
x=int(input())
#dp 테이블에 각 수가 1이 되기 위해서는 몇 번의 연산이 필요한지 저장
d=[0]*1000001
#0과 1은 1이 되기위한 연산과정이 없으므로 0으로 비움
for i in range(2,x+1):
  d[i]=d[i-1]+1
  if i % 2 ==0:
    d[i]=min(d[i],d[i//2]+1)
  if i % 3 ==0:
    d[i]=min(d[i],d[i//3]+1)

print(d[x])