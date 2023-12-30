# 절댓값 힙
# heap 모듈은 기본적으로 최소힙. 힙에 insert를 값이 아닌, 절댓값과 원본 값의 튜플 묶음을 사용.
import sys
from heapq import heappush,heappop
def input():return sys.stdin.readline().rstrip()

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0][1])
            heappop(heap)
    else:
        heappush(heap,(abs(num),num))

