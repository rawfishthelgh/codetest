from itertools import permutations
from collections import defaultdict

def solution(numbers):
    numlist = []
    for num in numbers:
        numlist.append(num)
    # print(numlist)
    answer = 0
    answers = defaultdict(int)
    for i in range(1, len(numbers)+1):
        # print(list(permutations(numlist,i)))
        numsets = list(permutations(numlist,i))
        for numset in numsets:
            num = ""
            for n in numset:
                num += n
            num = int(num)
            # print(num)
            if num > 1:
                if isPrime(num) :
                    if answers[num] == 0:   
                        answer += 1
                        answers[num] += 1 

    return answer

def isPrime(num):
    for j in range(2,num):
        if num % j ==0:
            return False
    return True