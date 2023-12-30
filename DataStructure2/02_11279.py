# 최대 힙
# heapq는 기본적으로 최소힙을 구현함. 최대힙으로 사용시 부호를 반대로 넣어주는 식으로 활용 가능.
from heapq import heappop,heappush
import sys

def input():return sys.stdin.readline().rstrip()

heap = []

N = int(input())

for _ in range(N):
    num = int(input())
    if num > 0:
        heappush(heap,-num)
    else :
        if len(heap) > 0:
            print(-heap[0])
            heappop(heap)
        else:
            print(0)
