def solution(n):
    answer = []
    for _ in range(1,n+1):
        if _%2==1:
            answer.append(_)
    return answer