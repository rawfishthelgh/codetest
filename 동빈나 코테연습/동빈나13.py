#int n insert
n = int(input())
#all food info insert
array=list(map(int,input().split()))
#dp table reset to save all result
d=[0]*100
# do dynamic programming(bottom-up)
d[0]=array[0]
d[1]=max(array[0],array[1]) #choose big result than each other
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])
#print result
print(d[n-1])