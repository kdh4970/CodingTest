# 2045 ~ 2118
# stk에 있는 값들(과거 값)이 현재 값보다 작으면 stk에서 빼고, 해당 인덱스 위치에 시간 저장.
from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    q = deque([0])
    for time in range(1,len(prices)):
        p = prices[time]
        while q and prices[q[-1]] > p:
            decreased = q.pop()
            answer[decreased]= time - decreased
        q.append(time)
    for _ in q:
        answer[_] = len(prices) - _-1
    return answer