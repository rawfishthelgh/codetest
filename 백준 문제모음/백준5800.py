k=int(input())
for i in range(1,k+1):
  num=i
  grade=list(map(int,input().split()))
  classsize=grade.pop(0)
  maxgrd=max(grade)
  mingrd=min(grade)
  grade.sort(reverse=True)
  gapgrd=0
  for i in range(1,len(grade)):
    if grade[i-1]-grade[i]>gapgrd:
      gapgrd=grade[i-1]-grade[i]
  print("Class",num)
  print("Max {0}, Min {1}, Largest gap {2}".format(maxgrd,mingrd,gapgrd))