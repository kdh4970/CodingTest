# 0958 ~ 1053
# 1~N을 순회
# stk 마지막 또는 컨테이너 첫번째에 현재 타겟이면 제거. 아니면 컨테이너 택베를 stk에 하나씩 삽입.
from collections import deque

def solution(order):
    answer = 0
    stk = []
    N = len(order)
    q = deque([x for x in range(1,N+1)])
    
    for target in order:
        stop = False
        while True:
            if q and q[0] == target:
                q.popleft()
                # print(f"pick {q.popleft()}")
                answer +=1
                break
            if stk and stk[-1] == target:
                # print(f"pick {stk.pop()}")
                stk.pop()
                answer +=1
                break
            if not q:
                stop = True
                break
            stk.append(q.popleft())
        if stop:break
    return answer