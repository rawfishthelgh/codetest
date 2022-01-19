n,c=map(int,input().split())
seq=list(map(int,input().split()))
nums={}
for i in range(n):
  num=seq[i]
  if num not in nums:
    nums[num]=1
  else:
    nums[num]+=1

cnt=[]
for i in nums.values():
  if i not in cnt:
    cnt.append(i)
cnt.sort(reverse=True)

for i in cnt:
  for x,y in nums.items():
    res=[]
    if i == y:
      for _ in range(y):
        res.append(x)
      for j in range(len(res)):
        print(res[j],end=" ")