# 2213 ~ 2258
# LRU는 가장 사용되지 않는 것을 후순위로 하며, 후순위는 배제 1순위
# 1 2 3에서 2가 호출되면, 2는 인덱스 +1 위치와 변경
# 빈도수 
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    N=len(cities)
    cache = deque()
    for _ in range(N):
        cities[_]=cities[_].lower()
    for city in cities:
        if city not in cache:
            answer += 5
            cache.append(city)
        else:
            answer += 1
            if cache.index(city)<cacheSize-1:
                idx = cache.index(city)
                temp = cache[idx]
                cache.remove(temp)
                cache.append(temp)
        if len(cache)>cacheSize:
            cache.popleft()
            

    return answer