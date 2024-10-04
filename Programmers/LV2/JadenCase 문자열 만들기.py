### Attempt 1 : 24.10.04
### Time : 1634 ~ 1701 (27m)

### solution
# 순회, 공백이 아니면 시작 추가
# 시작 점 있는데 공백 다시나오면 종료


def solution(s):
    answer = ''
    start=None
    for _ in range(len(s)):
        if start is None:
            if  s[_] != " ":
                start=_
                answer+=s[_].upper()
                continue
            else:
                answer += " "
        elif start is not None:
            if s[_] != " ":
                answer += s[_].lower()
                continue
            else:
                start=None
                answer+=" "
                continue
        
    return answer