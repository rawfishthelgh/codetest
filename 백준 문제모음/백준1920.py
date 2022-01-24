n=int(input())
a=list(map(int,input().split()))
m=int(input())
nums=list(map(int,input().split()))

a.sort()
#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid]==target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

#이진 탐색 수행 결과 출력
for num in nums:
  result=binary_search(a,num,0,n-1)
  if result == None:
      print(0,end=" ")
  else:
      #1 반환
      print(1,end=" ")