n,k=map(int,input().split())
hamlist=list(input())
cnt=0
for i in range(len(hamlist)):
  if hamlist[i]=='P':
    for j in range(max(0,i-k),min(n,i+k+1)):
      if hamlist[j]=='H':
        hamlist[j]='eat'
        cnt+=1
        break

print(cnt)