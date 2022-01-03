n=input()
col='abcdefgh'
row='12345678'
for i in range(len(col)):
  if n[0]==col[i]:
    x=i
for j in range(len(row)):
  if n[1]==row[j]:
    y=j
steps=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]

cnt=0
for step in steps:
  next_x=x+step[0]
  next_y=y+step[1]

  if next_x>=1 and next_x<=8 and next_y>=1 and next_y<=8:
    cnt+=1
print(cnt)

