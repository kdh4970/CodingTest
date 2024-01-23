# 미로 탐색
# BFS로 시점 근처부터 이동거리 체크, 가장먼저 종점에 도착할때가 최단거리.

import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

def can_go(map,arr,curr,cost):
    rows = len(map)
    cols = len(map[0])
    now_r, now_c = curr
    if now_r > 0 and map[now_r-1][now_c] == 1:
        map[now_r-1][now_c] = cost-1
        arr.append((now_r-1, now_c))
    if now_r < rows-1 and map[now_r+1][now_c] == 1:
        map[now_r+1][now_c] = cost-1
        arr.append((now_r+1, now_c))
    if now_c > 0 and map[now_r][now_c-1] == 1:
        map[now_r][now_c-1] = cost-1
        arr.append((now_r, now_c-1))
    if now_c < cols -1 and map[now_r][now_c+1] == 1:
        map[now_r][now_c+1] = cost-1
        arr.append((now_r, now_c+1))
    return map,arr

def bfs(map:list,start:tuple,end:tuple):
    q = deque([start])
    cost = 0
    while q:
        curr_row, curr_col = q.popleft()
        if map[curr_row][curr_col] == 1:
            cost -= 1
            map[curr_row][curr_col] = cost
        cost = map[curr_row][curr_col]
        map,q = can_go(map,q,(curr_row,curr_col),cost)
        if end in q:
            return map[end[0]][end[1]] * -1

N,M = list(map(int,input().split()))
board = []
for _ in range(N):
    input_s=input()
    board.append([int(s) for s in input_s])

start_point = (0,0)
end_point = (N-1,M-1)

distance = bfs(board,start_point,end_point)
print(distance)


