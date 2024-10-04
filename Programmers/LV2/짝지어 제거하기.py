### Attempt 1 : 24.10.04
### Time : 2105 ~ 2112 / 2117 ~ 2119 (9m)

### solution
# 스택에 넣으면서 중복시 스택팝

def solution(s):
    stk = []
    while True:
        for _ in s:
            if stk:
                if stk[-1]==_: stk.pop()
                else:stk.append(_)
            else:
                stk.append(_)
        temp ="".join(stk)
        if temp==s: break
        s=temp
        stk=[]
    return 0 if s else 1