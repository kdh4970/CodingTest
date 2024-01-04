# 스택 수열
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
res = []
stack = []
isValid = True


num=1
for _ in range(n):
    target = int(input())
    while 1:
        if len(stack) > 0:
            if stack[-1] == target:
                res.append("-")
                stack.pop()
                break
            if stack[-1] < target:
                res.append("+")
                stack.append(num)
                num+=1
                continue
            if stack[-1] > target:
                isValid = False
                break
        else:
            res.append("+")
            stack.append(num)
            num+=1

if isValid:
    for _ in res:
        print(_)
else:
    print("NO")

