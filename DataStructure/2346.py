# 풍선 터뜨리기

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = deque(enumerate(map(int,input().split())))


res = []

for _ in range(N):
    idx,offset = q.popleft()
    res.append(idx+1)

    if offset > 0:
        q.rotate(-offset+1)
    elif offset < 0:
        q.rotate(-offset)
    
print(*res)
