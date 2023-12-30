# 이중 우선순위 큐
# 최소힙으로 구현된 heapq의 마지막 노드가 최댓값이라는 보장이 없다!
# 최대힙으로 구현된 heapq 역시 마찬가지! 마지막 노드가 최소라는 보장이 없다.

import sys
from heapq import heappush,heappop
def input():return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    k=int(input())
    visited = [False] * k  # 원소의 삭제여부 저징
    maxheap = [] # 최댓값을 위합 맥스 힙
    minheap = [] # 최솟값을 위한 민 힙
    for __ in range(k):
        cmd = input()
        action, val = cmd.split()
        if action == "I":
            heappush(maxheap,(-int(val),__)) 
            heappush(minheap,(int(val),__)) 
            visited[__] = True
        elif action == "D":
            if val == "1":
                # !! 여기는 각 힙에서 삭제된 원소가 있는지 유효성 검사 및 처리 !!
                while maxheap and not visited[maxheap[0][1]]:
                    heappop(maxheap)
                if maxheap:# 유효성 처리 후 값이 남았다면 삭제 수행
                    visited[heappop(maxheap)[1]] = False
            elif val == "-1":
                while minheap and not visited[minheap[0][1]]:
                    heappop(minheap)
                if minheap:# 유효성 처리 후 값이 남았다면 삭제 수행
                    visited[heappop(minheap)[1]] = False
            else:
                pass
        else:
            pass
    # !! 여기는 삭제 작업 수행 후 결과로 사용하기 위해 다시한번 유효성 검사 및 처리 !!
    while minheap and not visited[minheap[0][1]]:
        heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heappop(maxheap)
    if not maxheap and not minheap:
        print("EMPTY")
    else:
        print(-maxheap[0][0],minheap[0][0])

