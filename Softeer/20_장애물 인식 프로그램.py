import sys
from collections import deque

n = int(input())
board = []
for _ in range(n):
    line = input()
    line = [int(x) for x in line]
    board.append(line)
visited = [[False] * n for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]

res = []

def bfs(r,c):
    q=deque([[r,c]])
    count = 0
    while q:
        now_r,now_c = q.popleft()
        # print(f"Searching ({now_r},{now_c})")
        if visited[now_r][now_c]:
            continue
        visited[now_r][now_c] = True
        count+=1
        for _ in range(4):
            new_r,new_c = now_r+dr[_], now_c+dc[_]
            if new_r < 0 or new_c < 0 or new_r > n-1 or new_c >n-1:
                continue
            if visited[new_r][new_c] or board[new_r][new_c]==0:
                continue
            q.append([new_r,new_c])
            # print(f"Pick ({new_r},{new_c})")
    res.append(count)
    
for r in range(n):
    for c in range(n):
        if not visited[r][c] and board[r][c] != 0:
            bfs(r,c)

print(len(res))
res.sort()
for _ in res:
    print(_)

