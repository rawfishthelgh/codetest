from collections import deque

def solution(priorities, location):
    answer = 0
    pdict = dict()
    q = deque()
    used = []
    maxq = []
    for i in range(len(priorities)):
        # 각 순서에 따른 우선순위 저장
        pdict[i] = priorities[i]
        # 큐에 저장
        q.append(i)
        # 각 우선순위값 저장
        maxq.append(priorities[i])
    # 최대 우선순위 순으로 정렬
    maxq.sort(reverse=True)

    while q :
        # 가장 왼쪽 요소 뺌
        now = q.popleft()
        # 해당 요소 가중치가 최댓값 아니면 다시넣음
        if pdict[now] < maxq[0]:
            q.append(now)
        # 최댓값이면 결과값에 요소 넣고 최댓값 삭제
        else:
            used.append(now)
            del maxq[0]
    # 해당 순서가 존재하는 인덱스 위치 찾음
    # 1번째부터 시작이므로 1 더함
    return used.index(location) + 1