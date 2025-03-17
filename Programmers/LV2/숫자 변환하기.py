# 1903 ~ 2104
# DP 
# 현재 값에 세가지 연산후 값 계산
# 세 값 중 목표값이 있으면, 저장
# 없으면 계속
from collections import deque
def solution(x, y, n):
    if x==y: return 0
    res = []
    q = deque([(x,0)])
    visited = set([x])
    while q:
        now,cnt = q.popleft()
        
        new = [now+n,now*2,now*3]
        for i in new:
            if i in visited:
                continue
            if i == y:
                res.append(cnt+1)
                break
            if i>y:
                break
            visited.add(i)
            q.append((i,cnt+1))
    return min(res) if res else -1