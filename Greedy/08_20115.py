# 에너지 드링크

import sys
def input():return sys.stdin.readline().rstrip()
N = int(input())
volume = sorted(list(map(int, input().split())),reverse=True)

res = volume[0]
for _ in range(1,N):
    if res >volume[_]:
        res += volume[_]/2
    else:
        res = volume[_] + res/2
print(res)