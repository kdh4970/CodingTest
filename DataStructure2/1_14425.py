# 문자열 집합

import sys

def input():return sys.stdin.readline().rstrip()

N,M = list(map(int,input().split()))

S = [input() for _ in range(N)]

cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1
print(cnt)