array=list(map(int,input()))

# #선택정렬
# for i in range(len(array)):
#   min=i
#   for j in range(i+1,len(array)):
#     if array[min]>array[j]:
#       min=j
#   array[i],array[min]=array[min],array[i]
# array.sort(reverse=True)
# for i in range(len(array)):
#   print(array[i],end="")

# #퀵정렬
# def quick_sort(array):
#   if len(array)<=1:
#     return array
  
#   pivot=array[0]
#   tail=array[1:]

#   left_side=[x for x in tail if x>=pivot]
#   right_side=[x for x in tail if x<pivot]

#   return quick_sort(left_side)+[pivot]+quick_sort(right_side)

# for i in quick_sort(array):
#   print(i,end="")

# #계수정렬
# cnt=[0]*(max(array)+1)

# for i in range(len(array)):
#   cnt[array[i]]+=1

# for i in range(len(cnt)-1,-1,-1):
#   for j in range(cnt[i]):
#     print(i,end="")