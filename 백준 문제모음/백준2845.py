l,p=map(int,input().split())
nums=list(map(int,input().split()))
full=l*p
for i in nums:
    print(i-full,end=" ")