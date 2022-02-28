def solution(matrix):
      collist=[]
  rowmidlist=[]
  colmidlist=[]
  for i in matrix:
    sorted_=sorted(i)
    mindex=len(sorted_)//2
    rowmidlist.append(sorted_[mindex])
  
  for i in range(len(matrix)):
    temp=[]
    for j in range(len(matrix)):
      temp.append(matrix[j][i])
    collist.append(temp)
  
  for i in collist:
    sorted_=sorted(i)
    mindex=len(sorted_)//2
    colmidlist.append(sorted_[mindex])
  
  answer=0
  for i in rowmidlist:
    for j in colmidlist:
      if i==j:
        answer+=1
        break
  return answer
