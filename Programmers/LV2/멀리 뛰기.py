# 1526 ~ 1609
# 1,2로 구성된 배열 생성.
# 1로만 가는 경우, 2로만 가는 경우(짝수 한정), 1과2 가 섞여서
# 1 (1): 1
# 2 (2): 11 2
# 3 (3): 111 12 21   
# 4 (5): 1111 112 121 211 22
# 5 (8) 11111 1112 1121 1211 2111 221 212 122
# 6 (13) 111111 11112*5 1122 1221 2211 1212 2112 2121  222
# 피보나치


import sys
sys.setrecursionlimit(10000)

arr=[1,2]

def func(n,step):
    global arr
    if step == n:
        return
    else:
        arr.append(arr[-1]+arr[-2])
        func(n,step+1)
    
            
def solution(n):
    if n<=2:
        return arr[n-1]
    func(n,2)
    return arr[n-1] % 1234567
    
    