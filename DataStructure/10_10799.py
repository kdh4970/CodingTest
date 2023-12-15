# 쇠막대기

import sys

def input():return sys.stdin.readline().rstrip()

data = input() 

res = 0
stack = []
for _ in range(len(data)):
    if data[_] == "(":
        stack.append(data[_])
        prior = data[_]
    else:
        if data[_-1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res +=1
        prior = data[_]
print(res)
