# 쇠막대기

import sys

def input():return sys.stdin.readline().rstrip()

data = input() 

res = 0
stack = []
prior = ""
for _ in data:
    if _ == "(":
        stack.append(_)
        prior = _
    else:
        if prior == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res +=1
        prior = _
print(res)
