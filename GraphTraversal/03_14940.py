# 쉬운 최단거리, BFS
from collections import deque
from copy import deepcopy
import sys

def input():
    return sys.stdin.readline().rstrip()

def can_go(map,curr,arr,dist):
    rows = len(map)
    cols = len(map[0])
    now_r,now_c = curr
    if now_r > 0 and map[now_r-1][now_c]==-1:
        arr.append((now_r-1,now_c))
        map[now_r-1][now_c] = dist+1
    if now_r < rows-1 and map[now_r+1][now_c]==-1:
        arr.append((now_r+1,now_c))
        map[now_r+1][now_c] = dist+1
    if now_c >0 and map[now_r][now_c-1]==-1:
        arr.append((now_r,now_c-1))
        map[now_r][now_c-1] = dist+1
    if now_c < cols-1 and map[now_r][now_c+1]==-1:
        arr.append((now_r,now_c+1))
        map[now_r][now_c+1] = dist+1
    return map,arr

def bfs(map,start):
    q = deque([start])
    dist=0
    while q:
        curr_r,curr_c = q.popleft()
        if map[curr_r][curr_c] == -2:
            map[curr_r][curr_c] = dist
        else:
            dist = map[curr_r][curr_c]
        map,q = can_go(map,(curr_r,curr_c),q,dist)

n,m = list(map(int, input().split()))
start = []
board = []
for _ in range(n):
    l = list(map(lambda x : -int(x), input().split()))
    if -2 in l:
        start = [_,l.index(-2)]
    board.append(l)
new_board = deepcopy(board)

bfs(board,start)
for _ in board:print(*_)
