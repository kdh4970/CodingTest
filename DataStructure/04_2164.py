# 카드2

import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

N = int(input())
q = deque([x+1 for x in range(N)])

# 첫 카드를 버림. 이후 가장 앞 카드를 가장 뒤로 이동.
while len(q) > 1:
    q.popleft()
    q.append(q[0])
    q.popleft()
print(q[0])
    
    
    
    
    
    