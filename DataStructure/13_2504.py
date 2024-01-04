# 괄호의 값

import sys
def input():
    return sys.stdin.readline().rstrip()

bracket = input()
stack = []
res = 0
temp = 1

for _ in range(len(bracket)):
    i = bracket[_]
    if i == "(":
        stack.append(i)
        temp *= 2
    elif i == "[":
        stack.append(i)
        temp *= 3
    elif i == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if bracket[_-1] == "(":
            res += temp
        stack.pop()
        temp //= 2
    elif i == "]":
        if not stack or stack[-1] == "(":
            res = 0
            break
        if bracket[_-1] == "[":
            res += temp
        stack.pop()
        temp //= 3

if stack: 
    print(0)
else: print(res)


