# 주유소

import sys
def input():return sys.stdin.readline().rstrip()

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))


c=price[0]
res = c * dist[0]
for _ in range(1,N-1):
    if c > price[_]:
        c = price[_]
    res += c* dist[_]

print(res)