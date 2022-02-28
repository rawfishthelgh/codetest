import sys
from collections import defaultdict
input = sys.stdin.readline


n,d,k,c=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.extend(arr)
left=0
right=0
result=0
dict_=defaultdict(int)
#보너스는 먹어야함
dict_[c] +=1

#처음 0부터 k만큼 먹어줌
while right<k:
  dict_[arr[right]] += 1
  right+=1
#left와 right를 1씩 늘려가면 전 구간에서 k만큼 먹는 값 갱신
while right < len(arr):
  #dict_의 길이는 해당 구간에서 먹은 초밥의 종류
  result=max(result,len(dict_))
  #맨 왼쪽 초밥 제거(left가 1 늘어났으니까 
  # 기존 맨 왼쪽은 없어져야함)
  dict_[arr[left]]-=1
  #제거해서 0이 됐으면 해당 인덱스에는
  #보너스가 없다는 뜻이므로 삭제
  if dict_[arr[left]]==0:
    del dict_[arr[left]]
  #right 1 늘어났으므로 오른쪽 초밥 추가
  dict_[arr[right]]+=1
  left+=1
  right+=1
print(result)
  
