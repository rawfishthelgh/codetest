import sys
from bisect import bisect_left,bisect_right
n=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
m=int(input())
nums=list(map(int,sys.stdin.readline().split()))
array.sort()
result=[]

def count_by_range(array,left_value,right_value):
  right_index=bisect_right(array,right_value)
  left_index=bisect_left(array,left_value)
  return right_index - left_index

for i in nums:
  print(count_by_range(array,i,i),end=" ")