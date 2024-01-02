# 최댓값

import sys
def input():return sys.stdin.readline().rstrip()

num = [int(input()) for _ in range(9)]

print(max(num))
print(num.index(max(num))+1)