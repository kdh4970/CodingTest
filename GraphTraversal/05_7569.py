# 토마토
# 시간제한 1초, 러닝타임 1156ms
import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def can_go(map,curr,arr,dist):
    depth,rows,cols = len(map),len(map[0]),len(map[0][0])
    now_d,now_r,now_c = curr
    if now_d > 0 and map[now_d-1][now_r][now_c] == 0:
        arr.append((now_d-1,now_r,now_c))
        map[now_d-1][now_r][now_c] = dist+1
    if now_d < depth-1 and map[now_d+1][now_r][now_c] == 0:
        arr.append((now_d+1,now_r,now_c))
        map[now_d+1][now_r][now_c] = dist+1
    if now_r > 0 and map[now_d][now_r-1][now_c] == 0:
        arr.append((now_d,now_r-1,now_c))
        map[now_d][now_r-1][now_c] = dist+1
    if now_r < rows -1 and map[now_d][now_r+1][now_c] == 0:
        arr.append((now_d,now_r+1,now_c))
        map[now_d][now_r+1][now_c] = dist+1
    if now_c > 0 and map[now_d][now_r][now_c-1] == 0:
        arr.append((now_d,now_r,now_c-1))
        map[now_d][now_r][now_c-1] = dist+1
    if now_c < cols -1 and map[now_d][now_r][now_c+1] == 0:
        arr.append((now_d,now_r,now_c+1))
        map[now_d][now_r][now_c+1] = dist+1
    return map,arr

def bfs3d(map,start):
    q = deque(start)
    dist = 0
    while q:
        now = q.popleft()
        dist = map[now[0]][now[1]][now[2]]
        map,q = can_go(map,now,q,dist)
    
    return map

def main():
    M,N,H = list(map(int,input().split()))
    board3d = []
    start = []
    isAlready = True
    for _ in range(H):
        board2d = []
        for __ in range(N):
            l = list(map(int,input().split()))
            if 0 in l:
                isAlready = False
            for ___ in range(M):
                if l[___] == 1:
                    start.append((_,__,___))
            board2d.append(l)
        board3d.append(board2d)

    if isAlready:
        print(0)
        return
    board3d = bfs3d(board3d,start)

    day = 0
    for _ in range(H):
        for __ in range(N):
            if 0 in board3d[_][__]:
                print(-1)
                return
            day = max(*board3d[_][__],day)
    print(day-1)


if __name__=="__main__":
    main()