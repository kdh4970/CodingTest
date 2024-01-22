# 그림
# stack 기반 dfs

import sys
def input():return sys.stdin.readline().rstrip()

n,m = list(map(int, input().split()))

def search_and_update(draw,curr,arr):
    now_r, now_c = curr
    if now_r > 0 and draw[now_r-1][now_c] == 1:
        arr.append((now_r-1, now_c))
    if now_r < n-1 and draw[now_r+1][now_c] == 1:
        arr.append((now_r+1, now_c))
    if now_c > 0 and draw[now_r][now_c-1] == 1:
        arr.append((now_r, now_c-1))
    if now_c < m-1 and draw[now_r][now_c+1] == 1:
        arr.append((now_r, now_c+1))
    return arr

def dfs(draw,start):
    stk = [start]
    area = 0
    while stk:
        curr = stk.pop(-1)
        if draw[curr[0]][curr[1]] ==1:
            draw[curr[0]][curr[1]] = -1
            area += 1
        stk = search_and_update(draw,curr,stk)
    return draw, area

draw = [list(map(int,input().split())) for _ in range(n)]

res = []
for row in range(n):
    for col in range(m):
        if draw[row][col] == 1 :
            draw, area = dfs(draw,(row,col))
            res.append(area)

print(len(res))
print(max(res) if res else 0)