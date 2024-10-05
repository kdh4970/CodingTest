### Attempt 1 : 24.10.05
### Time : 1635 ~ 1652 (17m)

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people=deque(people)
    cnt=0
    while people:
        w=people.pop()
        if people:
            if w+people[0] <=limit:
                w+=people.popleft()
            else:
                pass
        cnt+=1
        
        
    return cnt