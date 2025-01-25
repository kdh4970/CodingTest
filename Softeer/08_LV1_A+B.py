import sys

numT = int(input())
T = [list(map(int,input().split())) for _ in range(numT)]
for _ in range(numT):
    print(f"Case #{_+1}: {sum(T[_])}")