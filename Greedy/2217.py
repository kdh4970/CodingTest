# 로프

import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
rope = sorted([int(input()) for _ in range(N)])

res = 0
for _ in range(N):
    temp = (N-_) * rope[_]
    if temp > res:
        res = temp
print(res)