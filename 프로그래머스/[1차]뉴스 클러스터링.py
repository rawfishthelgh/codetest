from collections import defaultdict
import math

def solution(str1, str2):
    str1list = []
    str2list = []
    wdict1 = defaultdict(int)
    wdict2 = defaultdict(int)
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            str1list.append(temp.lower())
            wdict1[temp.lower()] += 1
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha():
            str2list.append(temp.lower())
            wdict2[temp.lower()] += 1

    #합집합구하기
    u_temp = str1list.copy()
    u_result = str1list.copy()
    for i in str2list :
        if i not in u_temp:
            u_result.append(i)
        else:
            u_temp.remove(i)
    #교집합구하기
    i_result = []
    for i in str2list:
        if i in str1list:
            str1list.remove(i)
            i_result.append(i)
    
    if len(i_result) ==0 and len(u_result) ==0:
        return 65536
    return math.floor((len(i_result)/len(u_result)) * 65536)