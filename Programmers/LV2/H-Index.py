# 2058 ~ 2108
# 내림차순 정렬
# X번째 논문(인덱스 X-1)의 인용수 K 일때,
# K>=h, X>=h 인 h의 최댓값
# 즉, min(K,X)의 최댓값

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h_max = 0
    for idx,val in enumerate(citations):
        h_max = max(h_max,min(idx+1,val))
    return h_max