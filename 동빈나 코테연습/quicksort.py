array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end: # 원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left = start +1 #피벗 다음이 left
    right = end # 맨 끝이 right
    while(left<=right):
        #피벗보다 큰 데이터 찾을때까지 반복
        #엇갈리지 않은 상태
        while(left<=end and array[left]<=array[pivot]):
            left += 1
        while(right > start and array[right]>=array[pivot]):
            right -= 1
        if (left>right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행(재귀)
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)