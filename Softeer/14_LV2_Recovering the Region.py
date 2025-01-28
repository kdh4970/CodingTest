import sys

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

for r in range(N):
    s = ""
    for _ in range(N):
        print(r+1, end=" ")
    print("")