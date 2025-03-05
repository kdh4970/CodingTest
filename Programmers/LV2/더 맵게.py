# 2021 ~ 2043
# 갯수가 백만 이상, 작은 수만 리스트에서 뺌. -> 최소힙
# 1. heap으로 시간복잡도 낮추기
# 2. 조건 만족 여부를 모든 원소가 K보다 큰지 비교할 필요 없음. 최소힙이기에 첫번째 원소만 체크하면 됨.
from heapq import heappush,heappop,heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville)>1 and scoville[0]<K: 
        heappush(scoville,heappop(scoville)+(heappop(scoville)*2))
        answer +=1
    if scoville[0]<K:
        answer = -1
    return answer