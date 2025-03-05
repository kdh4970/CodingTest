# 2012 ~ 2020
# 2 3 3 5
# iter val
# 0 2
# 1 3
# 2 3
# 3 5
# 자신보다 뒤에 있는 큰 수 중 가장 가까운 것
# 자신보다 앞에 있는 작은 수 보다 클때, 이미 처리했으면 패스, 처리 안했으면 답에 저장.
# 해당 위치에 값을 저장해야 하므로, 값이 아닌 인덱스 저장
# 즉, 회차마다 해당 회차 인덱스를 넣어, 다름 차수의 값이랑 과거 차수 인덱스들에 대응되는 값을 비교. 단, 조건 부합시 빼야함. 
def solution(numbers):
    answer = [-1] * len(numbers)
    arr = [0]
    for i in range(1,len(numbers)):
        while arr and numbers[arr[-1]] < numbers[i]:
            answer[arr.pop()] = numbers[i]
        arr.append(i)
    return answer
