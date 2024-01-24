# 토마토
# 0 : 익지 않은 토마도
# 1 : 익은 토마도
# -1 : 빈 공간
# bfs, 다중 시작점

import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def can_go(map,curr,arr,dist):
    rows ,cols = len(map),len(map[0])
    now_r,now_c = curr
    if now_r > 0 and map[now_r-1][now_c] == 0:
        arr.append((now_r-1,now_c))
        map[now_r-1][now_c] = dist+1
    if now_r < rows - 1 and map[now_r+1][now_c] == 0:
        arr.append((now_r+1,now_c))
        map[now_r+1][now_c] = dist+1
    if now_c > 0 and map[now_r][now_c-1] == 0:
        arr.append((now_r,now_c-1))
        map[now_r][now_c-1] = dist+1
    if now_c < cols - 1 and map[now_r][now_c+1] == 0:
        arr.append((now_r,now_c+1))
        map[now_r][now_c+1] = dist+1
    return map,arr

def bfs(map,start):
    q=deque(start)
    dist = 1
    while q:
        now_r,now_c = q.popleft()
        dist = map[now_r][now_c]
        map,q = can_go(map,(now_r,now_c),q,dist)
    return map

def main():
    M,N = list(map(int,input().split()))
    board = []
    start = []
    for _ in range(N):
        l = list(map(int,input().split()))
        for __ in range(M):
            if l[__] == 1:
                start.append((_,__))        
        board.append(l)

    for idx,val in enumerate(board):
        if all(x for x in val):
            if idx == len(board)-1:
                print(0)
                return
            continue
        else: break

    board = bfs(board,start)
    day = 0
    for b in board:
        if 0 in b:
            print(-1)
            return
        day = max(*b,day)
    print(day-1)

if __name__=="__main__":
    main()


