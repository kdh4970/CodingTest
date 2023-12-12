# 2+1 세일

import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
price = [int(input()) for _ in range(N)]
price.sort(reverse=True)

res = 0
for _ in range(N):
    res += price[_] if (_%3 in [0,1]) and _+1 < N-N%3 else 0
res += price[N-1] if N%3 in [1,2] else 0
res += price[N-2] if N%3 == 2 else 0
print(res)