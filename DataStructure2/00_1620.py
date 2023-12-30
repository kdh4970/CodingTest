# 나는야 포켓몬 마스터 이다솜

import sys

def input(): return sys.stdin.readline().rstrip()

N,M = list(map(int,input().split()))

NumTooNameTable = dict()
NameToNumTable = dict()

for _ in range(1,N+1):
    temp = input()
    NameToNumTable[temp] = _
    NumTooNameTable[_] = temp

for _ in range(M):
    test = input()
    try:
        test = int(test)
        print(NumTooNameTable[test])
    except ValueError:
        print(NameToNumTable[test])
