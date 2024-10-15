def solution(array, height):
    answer = 0
    for _ in array:
        answer +=1 if _ >height else 0
    return answer