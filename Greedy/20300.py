# 서강근육맨

import sys
def input():return sys.stdin.readline().rstrip()
N = int(input())
t = sorted(list(map(int, input().split())))

minM = 0
if N%2 == 1:
    minM = t[-1]
    for _ in range(N//2):
        temp = (t[_] + t[N-2-_])
        minM = temp if temp > minM else minM
else:
    for _ in range(N//2):
        temp = (t[_] + t[N-1-_])
        minM = temp if temp > minM else minM
print(minM)
