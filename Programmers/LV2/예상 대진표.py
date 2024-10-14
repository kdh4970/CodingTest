# 2052 ~ 2128
# 번호
# 12에서 이기면 1번, 34에서 이기면 2번, 56(45)에서 이기면 3번
# 인덱스 x에서 이기면 (x-1) // 2 + 1  번
# 경기 후 두 선수가 만나는지 체크 : 차이가 1이면 -> 턴수 반환
# 1번 일때의 예외 처리
# 8 9 와 같은 경우의 예외처리
# 4 5
# 2 3
# 1 2

def func(turn,a,b):
    print(turn,a,b)
    if abs(a-b)==1 and (a//2 != b//2):
        return turn
    return func(turn+1, (a-1)//2 + 1 ,(b-1)//2 + 1)

def solution(n,a,b):
    answer = func(1,a,b)

    return answer