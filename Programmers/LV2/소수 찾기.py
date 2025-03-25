# 1523 ~ 1602
# 주어진 수들을 활용하여 만들 수 있는 소수의 수
# 1,7 이면 1과 7을 반드시 써야하는 것은 아니지만 적어도 하나는 사용해야 함.
# 그러면 첫번째를 확정적으로 숫자로 뽑고, 나머지 자리는 뽑지 않는 공백을 옵션에 추가
from math import sqrt

visited = []

def isPrime(x):
    if x in [0,1]: return False
    if x in [2,3]: return True
    for _ in range(2,int(sqrt(x))+1):
        if x % _ == 0:
            return False
    return True

def solution(numbers):
    global visited
    answer = set()
    visited = [False] * len(numbers)

    
    def func(nums,cnt):
        global visited
        if nums != "":
            answer.add(int(nums))
        if cnt == len(numbers):
            return
        for _ in range(len(numbers)):
            if not visited[_]: visited[_]=True;func(nums+numbers[_],cnt+1);visited[_]=False
    
    func("",0)
    print(answer)
    return sum([isPrime(int(_)) for _ in list(set(answer))])