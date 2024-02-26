# 인구이동 
# 시간제한 2초 / 실행 시간 4.9초
# 1. 연합이 가능한가? 가능하다면 그룹으로 묶기.
# 2. 연합이 불가능할 때 까지 반복
# 3. 소요된 날 수

import sys
from collections import deque

def input():return sys.stdin.readline().rstrip()

N,L,R = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
q = deque()
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

def bfs(x,y):
    q.append((x,y))
    union = []
    union.append((x,y))
    while q:
        now_x,now_y = q.popleft()
        for _ in range(4):
            temp_x = now_x + dx[_]
            temp_y = now_y + dy[_]
            if not 0 <= temp_x < N or not 0 <= temp_y < N or visited[temp_x][temp_y] == 1:
                continue
            if L <= abs(board[now_x][now_y] - board[temp_x][temp_y]) <= R:
                union.append((temp_x,temp_y))
                q.append((temp_x,temp_y))
                visited[temp_x][temp_y] = 1
        
    if len(union) > 1:
        result = sum(board[a][b] for a,b in union) // len(union)
        for a,b in union:
            board[a][b] = result
        return 1
    return 0

day = 0
while True:
    stop = 0
    visited = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = 1
                stop += bfs(row,col)
    if stop == 0:break
    day += 1

print(day)
