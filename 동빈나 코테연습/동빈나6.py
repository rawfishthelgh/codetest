#현재 나이트의 위치 입력
input_data=input()#문자열로 입력
row=int(input_data[1])#현재 행 위치
#문자 아스키코드로 변환한값-a를 아스키코드로 변환한값=현재 열 위치
column=int(ord(input_data[0]))-int(ord('a'))+1

#나이트가 이동할 수 있는 8가지 방향
steps=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

#8가지 방향에 대해 각 위치로 이동 가능한지 확인
cnt=0
for step in steps:
  #이동하려는 위치 확인
  next_row = row+step[0] #행 목적지
  next_column = column+step[1] #열 목적지

  #해당 위치 이동 가능하면 카운트 증가, 1부터 8 범위 안에 들어야 함
  if next_row >= 1 and next_row<=8 and next_column >=1 and next_column<=8:
    cnt+=1

print(cnt)