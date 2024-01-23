# 단지번호붙이기
# bfs

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def can_go(map,curr,arr):
    rows = len(map)
    cols = len(map[0])
    now_r, now_c = curr
    if now_r > 0 and map[now_r-1][now_c] == 1:
        map[now_r-1][now_c] = 0
        arr.append((now_r-1,now_c))
    if now_r < rows - 1 and map[now_r+1][now_c] == 1:
        map[now_r+1][now_c] = 0
        arr.append((now_r+1,now_c))
    if now_c > 0 and map[now_r][now_c-1] == 1:
        map[now_r][now_c-1] = 0
        arr.append((now_r,now_c-1))
    if now_c < cols - 1 and map[now_r][now_c+1] == 1:
        map[now_r][now_c+1] = 0
        arr.append((now_r,now_c+1))
    return map,arr

def bfs(map,start):
    q = deque([start])
    count = 0
    while q:
        count += 1
        now = q.popleft()
        map[now[0]][now[1]] = 0
        map,q = can_go(map,now,q)
    return map,count

N = int(input())
board = []
for _ in range(N):
    input_s = input()
    board.append([int(s) for s in input_s])

building = []

for row in range(N):
    for col in range(N):
        if board[row][col]:
            board,count = bfs(board,(row,col))
            building.append(count)

print(len(building))
building.sort()
for _ in building:
    print(_)