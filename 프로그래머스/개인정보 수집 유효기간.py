#초기풀이
def solution(today, terms, privacies):
    answer = []
    termsdict = dict()
    for term in terms:
        termsdict[term[0]] = int(term[2:])
    
    today = list(map(int,today.split(".")))
    todayYear = today[0]
    todayMonth = today[1]
    todayDay = today[2]
    for i in range(len(privacies)):
        date = list(map(int,privacies[i][:10].split(".")))
        term = privacies[i][-1]
        termMonth = termsdict[term] # 유효 개월 수
        # print("termMonth",termMonth)
        nowYear = date[0]
        nowMonth = date[1]
        nowDay = date[2]
        # print(nowYear,nowMonth,nowDay)
        for _ in range(termMonth) :
            nowMonth+=1
            if (nowMonth>12):
                nowYear += 1
                nowMonth = 1
        if nowYear<todayYear:
            answer.append(i+1)
            continue
        if nowYear>todayYear:
            continue
        if nowMonth<todayMonth:
            answer.append(i+1)
            continue
        if nowMonth>todayMonth:
            continue
        if nowDay<=todayDay:
            answer.append(i+1)
            continue
        if nowDay>todayDay:
            continue
    return answer

#개선풀이

def solution(today, terms, privacies):
    answer = []
    termsdict = dict()
    for i in terms:
        term = list(i.split(" "))
        termsdict[term[0]] = int(term[1])*28
    today = list(map(int,today.split(".")))
    todayDay = (today[0]*12*28)+(today[1]*28)+today[2]
    for i in range(len(privacies)):
        now,term = privacies[i].split(" ")
        nowdate = list(map(int,now.split(".")))
        possibleDay = (nowdate[0]*12*28)+(nowdate[1]*28)+nowdate[2] + termsdict[term]

        if todayDay>=possibleDay:
            answer.append(i+1)
    return answer