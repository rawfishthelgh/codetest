n=int(input())
cityfar=list(map(int,input().split()))
price=list(map(int,input().split()))

totalprice=0
nowprice=price[0]

for i in range(n-1):
  if price[i]<nowprice:
    nowprice = price[i]
  totalprice += nowprice * cityfar[i]

print(totalprice)