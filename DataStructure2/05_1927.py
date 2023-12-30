# 최소 힙
from heapq import heappush,heappop
import sys
def input():return sys.stdin.readline().rstrip()

N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heappush(heap,num)
    elif num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heappop(heap)


