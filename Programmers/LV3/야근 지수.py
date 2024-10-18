# 1550 ~ 1705
# 피로도 = 시작시점에서 남은 작업량 제곱을 더함
# 제곱으로 더해지기 때문에, 작업량의 최댓값부터 처리해야함.
# reverse sort
# 0번에 최댓값 하나 인경우 : 1번과 0번의 차 만큼 일 수행
# 0번과 x 번까지 동일한 최댓값인 경우, 순차적으로 1 빼기
# 

from heapq import heappush,heappop,heapify

def solution(n, works):
    answer = 0
    n_works = len(works)
    work_heap =[]
    for work in works:
        heappush(work_heap,-work)
    while n>0:
        # if list(set(work_heap))==[0]:
        #     break
        # print(work_heap)
        w = heappop(work_heap)
        if w==0:
            break
        heappush(work_heap,w+1)
        n-=1
    
    # print(work_heap)
    
    return sum(map(lambda x: x**2 ,work_heap))