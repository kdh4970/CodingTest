### Attempt 1 : 24.10.04
### Time : 1737 ~ 1754 (27m)

### solution
# 함수(i,n) : i 부터 연속 수 합이 n인게 존재하는지 체크 -> 초과 False, 만족 True
# 루프 함수(0,n) 부터 함수(n//2,n) 까지 하고 +1

def func(i,n):
    lst=[]
    for _ in range(i,n//2+2):
        lst.append(_)
        if sum(lst) == n:
            print(lst)
            return True
        elif sum(lst) > n:
            return False
    return False
def solution(n):
    answer = 0
    for _ in range(1,n//2+1):
        answer += func(_,n)
    answer += 1
    return answer