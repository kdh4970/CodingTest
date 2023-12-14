# 요세푸스 문제

from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N,K = map(int, input().split())

q=deque([x for x in range(1,N+1)])
res = []
while len(q) !=0:
    q.rotate(-K)
    res.append(q[-1])
    q.pop()
print("<" + ", ".join(map(str, res)) + ">")

