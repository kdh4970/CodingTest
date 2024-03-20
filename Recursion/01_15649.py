# N과 M (1)
# 시간제한 1초
import sys
def input():return sys.stdin.readline().rstrip()

N,M = list(map(int, input().split()))

arr = []

def func(x):
    if x == M:
        print(*arr)
        return
    for _ in range(1,N+1):
        if _ not in arr:
            arr.append(_)
            func(x+1)
            arr.pop()
    
func(0)
