# 블로그2

import sys
def input():return sys.stdin.readline().rstrip()
N = int(input())
target = input()
countB = target.count("B")
countR = target.count("R")
cnt=1
if countR>countB:
    for idx,val in enumerate(target):
        if val == "B":
            cnt += 1 if target[idx-1] == "R" else 0
else:
    for idx,val in enumerate(target):
        if val == "R":
            cnt += 1 if target[idx-1] == "B" else 0
            
print(cnt)