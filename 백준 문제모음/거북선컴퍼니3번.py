def solution(n, r, c):
      matrix=[[0]*n for _ in range(n)]
  
  row=[]
  col=[]
  
  for i in range(n):
    row.append(i)
    col.append(i)
  
  left=0
  right=1
  rowindex=[]
  colindex=[]
  num=1
  while left != n:
    temp=[]
    for x in range(left,right):
      temp.append(x)
    if right<n:
      right+=1
    else:
      left+=1
    rowindex.append(temp)
    revtemp=list(reversed(temp))
    colindex.append(revtemp)
  
  for time in range(len(rowindex)):
    for i in range(len(rowindex[time])):
      x=rowindex[time][i]
      y=colindex[time][i]
      if time%2 != 0:
        matrix[x][y]=num
      else:
        matrix[y][x]=num
      num+=1
  answer=matrix[r-1][c-1]
  return answer

print(solution(5,3,2))