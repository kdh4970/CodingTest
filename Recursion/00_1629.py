# 곱셈 
# 시간제한 0.5초
## a^(N+M) = a^N * a^M
## (a*b)%c = (a%c * b%c)%c
## 너무 어렵다
import sys
def input():return sys.stdin.readline().rstrip()

A,B,C = list(map(int,input().split()))


def func(a,b):
    if b==1:
        return a%C
    res = func(a,b//2)
    if b%2 == 0:
        return (res*res)%C
    else:
        return (res*res*a)%C

print(func(A,B))
