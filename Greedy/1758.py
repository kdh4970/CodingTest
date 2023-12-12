# 알바생 강호

import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
t = [int(input()) for _ in range(N)]
t = sorted(t,reverse=True)
res = 0
for _ in range(N):
    res += 0 if t[_]-(_) < 0 else t[_]-(_)
print(res)