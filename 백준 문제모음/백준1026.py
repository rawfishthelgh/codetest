n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
ans=0
for i in range(len(a)):
    ans += a[i]*max(b)
    b.pop(b.index(max(b)))
print(ans)