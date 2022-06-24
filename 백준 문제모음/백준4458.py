import sys
input= sys.stdin.readline

n=int(input())
wordlist=[]

for _ in range(n):
  word=input()
  newword=word[0].upper()+word[1:]
  wordlist.append(newword)


for i in range(len(wordlist)):
  print(wordlist[i].strip())