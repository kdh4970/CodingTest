# 1746 ~ 1806

# 1 2 3 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4
# r,c의 최댓값을 기입.

# 1차원 배열화

# 애초에 1차원 배열로 만들고 인덱스를 계산
## n이 10의 7승이므로, 이렇게 큰 값은 무지성 구현으로는 불가능
# 반드시 로직 압축, 알고리즘 개선 필요.

def solution(n, left, right):
    answer = []
    for _ in range(left,right+1):
        r,c = _//n,_%n
        answer.append(max(r,c) + 1)
    return answer