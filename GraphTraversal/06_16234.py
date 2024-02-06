# 인구이동
# 1. 연합이 가능한가? 가능하다면 그룹으로 묶기.
# 2. 연합이 불가능할 때 까지 반복
# 3. 소요된 날 수

import sys
from collections import deque

def input():return sys.stdin.readline().rstrip()

N,L,R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q.append((x,y))
    union = []
    union.append((x,y))
    while q:
        a,b = q.popleft()
        for _ in range(4):
            na = a + dx[_]
            nb = b + dy[_]
            if na<0 or nb<0 or na>N-1 or nb>N-1 or visited[na][nb] == 1:
                continue
            if L <= abs(board[a][b] - board[na][nb]) <= R:
                visited[na][nb] = 1
                q.append((na,nb))
                union.append((na,nb))
    if len(union)>1:
        result=sum(board[a][b] for a,b in union) // len(union)
        for a,b in union:
            board[a][b] = result
        return 1
    else:
        return 0

days = 0
while True:
    stop = 0
    visited = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = 1
                stop += bfs(row,col)
    if stop == 0:
        break
    days += 1
print(days)
