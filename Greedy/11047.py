# 동전 0

import sys
def input(): return sys.stdin.readline().rstrip()

N,K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
cnt = 0
sum = 0
for coin in coins:
    if coin > K or sum + coin > K:continue
    cnt += (K-sum) // coin
    sum += coin * ((K-sum) // coin)


print(cnt)