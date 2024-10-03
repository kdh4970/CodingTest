### Attempt 1 : 24.10.03
### Time : 1720 ~ 1756 (36m)

### solution
# 리스트 순회 : 스택에 하나씩 넣기
# 1231 구성 시 제거.

def solution(ingredient):
    answer = 0
    stk = []
    for _ in ingredient:
        if len(stk)>=3 and stk[-3]==1 and stk[-2]==2 and stk[-1]==3 and _==1:
            stk.pop()
            stk.pop()
            stk.pop()
            answer += 1
            continue
        stk.append(_)
    return answer