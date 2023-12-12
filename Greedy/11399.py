# ATM

import sys
def input():return sys.stdin.readline().rstrip()

N = int(input())
p = list(map(int, input().split()))
p = sorted(p)

res=0
for _ in range(N):
    res += p[_]*(N-_)
print(res)
