# 1627 ~ 1647
# 부분수열의 합의 가짓수 + 로테이션 포함
# 현재 턴에 대해 부분수열의 합의 가짓수를 먼저 구하고, 매 로테이션마다 0부터 n까지 합들을 계산
# 1. 연속부분수열 구하기.
# 2. 합을 set에 저장
# 3. 로테이션 후 합을 set에 저장
# 4. set의 길이 반환

from collections import deque

def solution(elements):
    n = len(elements)
    sum_arr = set()
    for i in range(n):
        for f in range(i+1,n+1):
            arr = elements[i:f]
            sum_arr.add(sum(arr))
    #rotation
    elements = deque(elements)
    for rot in range(n-1):
        elements.rotate(1)
        lst = list(elements)
        for i in range(1,n):
            arr=lst[:i]
            sum_arr.add(sum(arr))
    
    
    return len(sum_arr)


## 더 나은 코드
# 인덱스가 갯수 초과 하는 경우를 나머지를 활용하여 처리
# 이로인해 덱을 만드는 것, 회전 시키는 과정이 필요 없어짐.
# 결과적으로 시간복잡도가 줄어듬.
# 위 코드는 최대 7초, 아래 코드는 350ms 이내에 완료됨.



def solution(elements):
    n = len(elements)
    sum_arr = set()
    for i in range(n):
        sum_arr.add(elements[i])
        lst = elements[i]
        for j in range(i+1,i+n):
            lst += elements[j%n]
            sum_arr.add(lst)
    
    return len(sum_arr)