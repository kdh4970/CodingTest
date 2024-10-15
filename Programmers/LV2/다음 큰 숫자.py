### 1127 ~ 1133
# n보다 큰 자연수,
# n의 2진수에서의 1의 갯수와, n의 다음 큰 수의 2진수에서의 1의 갯수 동일


def solution(n):
    original = bin(n).count("1")
    step = n+1
    while True:
        compare = bin(step).count("1")
        if compare == original:
            break
        step +=1
        
    return step