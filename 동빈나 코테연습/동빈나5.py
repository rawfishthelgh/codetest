n=int(input())
cnt=0


for i in range(n+1):#i가 0부터 n까지 1씩 증가하도록
  for j in range(60):
    for k in range(60):
      #매 시각마다 3 포함되면 카운트 증가
      if '3' in str(i)+str(j)+str(k):
        cnt+=1

print(cnt)