# 1713 ~ 1724
# 큐의 맥스 계산 전 큐가 비어있지 않은지 먼저 체크 필요

from collections import deque

def solution(priorities, location):
    n = len(priorities)
    
    answer = 0
    q=deque(priorities)
    idxs = deque(list(range(n)))
    while q:
        p = q.popleft()
        idx = idxs.popleft()
        if q and p < max(q):
            q.append(p)
            idxs.append(idx)
        else:
            answer+=1
            if idx == location:
                break
    
    return answer