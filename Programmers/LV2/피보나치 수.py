### Attempt 1 : 24.10.04
### Time : 1959 ~ 2023 (24m)

### solution
# 피보나치 수 구하는 함수

fibo=[0,1]
def make_fibo(n):
    idx=1
    while idx<n:
        fibo.append(fibo[-1]+fibo[-2])
        idx+=1

def solution(n):
    make_fibo(n)
    return fibo[-1] % 1234567