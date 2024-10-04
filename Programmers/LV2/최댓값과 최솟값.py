### Attempt 1 : 24.10.04
### Time : 1325 ~ 1328 (3m)

### solution
# split -> min max print

def solution(s):
    s=list(map(int,s.split(" "))) 
    answer= f"{min(s)} {max(s)}"
    return answer