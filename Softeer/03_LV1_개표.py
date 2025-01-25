import sys

N = int(input())
counts = [int(input()) for _ in range(N)]

for count in counts:
    five,last = count//5, count%5
    print("++++ "*five+"|"*last)