n,k=map(int,input().split())
coin=[]
cnt=0
for i in range(n):
  a=int(input())
  coin.append(a)

coin.sort(reverse=True)
for i in coin:
  if(i>k):
    continue
  else:
    if (k % i != 0):
      cnt += k//i
      k %= i

    else:
      cnt += k//i
      k %= i

      break

print(cnt)