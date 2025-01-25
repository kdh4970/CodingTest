import sys

n = int(input())
towns = list(map(int,input().split()))

dist = [towns[d+1] - towns[d] for d in range(n-1)]
print(dist.count(min(dist)))