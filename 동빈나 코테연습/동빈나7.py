s=input()
result=[]
value=0
#문자 하나씩 확인
for x in s:
  #알파벳이면 리스트 삽입
  if x.isalpha():
    result.append(x)
  #숫자면 따로 더함
  else:
    value += int(x)
#알파벳 오름차순 정렬
result.sort()
#숫자가 하나라도 있으면 뒤에 삽입
if(value !=0):
  result.append(str(value))
#최종 결과 출력
print(''.join(result))