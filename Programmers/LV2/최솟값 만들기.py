### Attempt 1 : 24.10.04
### Time : 1332 ~ 1627 (175m)

### solution
# 최소와 최대가 곱해지도록


def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    return sum(list(map(lambda a,b:a*b,A,B)))