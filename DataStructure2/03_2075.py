# N번째 큰 수
import sys
from heapq import heappush,heappop
def input():return sys.stdin.readline().rstrip()

N = int(input())

mat = []

for _ in range(N):
    temp = list(map(int,input().split()))
    for __ in temp:
        if len(mat) < N:
            heappush(mat,__)
        else:
            if __ < mat[0]:
                pass
            else:
                heappop(mat)
                heappush(mat,__)
    
print(mat[0])