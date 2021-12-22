n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort() #오름차순 정렬
b.sort(reverse=True) #내림차순 정렬

#최대 k번 비교, 첫 인덱스부터 확인
for i in range(k):
  #a의 원소가 b의 원소보다 작은 경우
  if a[i]<b[i]:
    #두 원소를 됴체
    a[i],b[i]=b[i],a[i]
  else: #a의 원소가 b의 원소보다 크거나 같을 때 반복문 탈출
    break
print(sum(a))