# 2303 ~ 2422
from math import sqrt
def isPrime(x):
    if x<2: return False
    for _ in range(2,int(sqrt(x))+1):
        if x % _ ==0:
            return False
    return True

def solution(n, k):
    answer = 0
    lst = []
    divider = k
    while n> divider*k:
        divider *= k
    while n>0:
        lst.append(n//divider)
        n = n%divider
        divider//=k
    lst.append(n)
    
    n_str = "".join(map(str,lst))
    n_str = n_str.split("0")
    for s in n_str:
        if s in ["1",""]: continue
        if isPrime(int(s)): answer+=1
    
    return answer