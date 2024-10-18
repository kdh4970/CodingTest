# 1404~1420

from collections import deque
def solution(operations):
    answer = []
    q=[]
    for op in operations:
        action,value = op.split(" ")
        value = int(value)
        if action =="I":
            if q and value >=q[-1]:
                q.append(value)
            elif q and value <=q[0]:
                q.insert(0,value)
            else:
                q.append(value)
                q.sort()
        elif action=="D" and q:
            if value ==1:
                q.pop()
            elif value == -1:
                q.pop(0)
    if not q:
        answer = [0,0]
    else:
        answer = [max(q),min(q)]
    return answer