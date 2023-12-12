# 잃어버린 괄호

import sys
def input():return sys.stdin.readline().rstrip()
eq = list(map(str,input().split("-")))
num =[]
for _ in eq:
    if _.find("+")!=-1:
        num.append(sum(list(map(int,_.split("+")))))
    else:num.append(int(_))
res = num[0]-sum(num[1:])
print(res)