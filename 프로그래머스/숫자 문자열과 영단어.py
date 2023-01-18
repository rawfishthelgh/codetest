# 내 풀이
def solution(s):
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    wordMap = dict()
    for i in range(len(words)):
        wordMap[words[i]] = numbers[i]
    answer = ""
    left = 0
    right = 1
    while right <= len(s):
        if s[left].isdigit():
            answer+=s[left]
            left += 1
            right += 1
            continue
        if s[left:right] in wordMap.keys():
            answer+=wordMap[s[left:right]]
            left = right
            right += 1
        else:
            if s[right].isdigit():
                answer+=s[right]
                left = right + 1
                right += 1
                continue
            right += 1
    return int(answer)

# 좋은 풀이
def solution(s):
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    wordMap = dict()
    for i in range(len(words)):
        wordMap[words[i]] = numbers[i]
    answer = s
    for key, value in wordMap.items():
        answer = answer.replace(key,value)
    return int(answer)