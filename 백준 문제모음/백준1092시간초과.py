import sys
input=sys.stdin.readline
n=int(input())
cranes=list(map(int,input().split()))
m=int(input())
boxes=list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt=0


while len(boxes)!=0:
  for i in range(len(cranes)):
    for j in range(len(boxes)):
      if cranes[i]>=boxes[j]:
        boxes.pop(j)
        break
  cnt+=1

print(cnt)