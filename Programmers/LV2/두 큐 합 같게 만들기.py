# 1646 ~ 1731
# 두 큐의 합이 같아질때까지, 한쪽에선 빼고, 한쪽에선 삽입.
# 반복문 내에서 sum을 계속 연산하지 말고, 첫 계산 이후 더하고 빼기만 수행하여 시간초과 방지
# 
from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    target = sum(queue1+queue2)
    if target%2!=0:
        return -1
    target//=2
    
    q1=deque(queue1)
    q2=deque(queue2)
    count = 0
    limit = len(q1)*5
    s1,s2 = sum(q1),sum(q2)
    while True:
        if s1 == s2:
            break
        if s1 > s2:
            s1-=q1[0]
            s2+=q1[0]
            q2.append(q1.popleft())
        else:
            s1+=q2[0]
            s2-=q2[0]
            q1.append(q2.popleft())
        count+=1
        if count >limit:
            return -1
        
    return count