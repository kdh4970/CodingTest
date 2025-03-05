# 2119 ~ 2233
# 각 행에서 하나씩 뽑기. 단 열수가 중복되는 경우는 제외.
# 각 경우에서 점수 계산
# 각 행을 내려가며 누적합의 최대 계산. 단, 같은 열 제외
# 각 행의 누적합을 계산할때, 다음 값의 최대를 더하는 것 X
# 행의 각 열의 누적합을 계산할때, 이전 행의 최대값에 더해야 함.

def solution(land):
    for _ in range(1,len(land)):
        land[_][0] += max(land[_-1][1],land[_-1][2],land[_-1][3])
        land[_][1] += max(land[_-1][0],land[_-1][2],land[_-1][3])
        land[_][2] += max(land[_-1][0],land[_-1][1],land[_-1][3])
        land[_][3] += max(land[_-1][0],land[_-1][1],land[_-1][2])
    return max(land[-1])