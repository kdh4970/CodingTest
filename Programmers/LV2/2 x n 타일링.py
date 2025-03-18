# 1642 ~ 1710
# 1과2로 n 을 만드는 가지수
# 1 : 1
# 2 : 2
#     11     2
# 3 : 3
#     111    12 21
# 4 : 5
#     1111   121 211 112                   22
# 5 : 8
#     11111  2111 1211 1121 1112           221 212 122                      
# 6 : 13
#     111111 21111 12111 11211 11121 11112 2211 1221 1122 2121 2112 1212 222 


def solution(n):
    if n in [1,2]:
        return n
    def func(n,d):
        stk = [1,2]
        cnt = 2
        sig=True
        while cnt<n:
            if sig:
                stk[0] += stk[1]
                sig = not sig
            else:
                stk[1] += stk[0]
                sig = not sig
            cnt +=1
        return max(stk)
    
    return func(n,2)%1000000007