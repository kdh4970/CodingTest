# 1603 ~ 1720

# dp배열 [i][j] = dp[i-1][j] + dp[i][j-1]
# bfs를 1,1 의 값 1로 시작
# 일단 웅덩이인지 확인,
# 아니라면 dp 업데이트
# 좌표를 m,n이라 하였음. 즉 r,c가 아닌 x,y로 생각.
# 특정값 나누기 A=B+C 일 때, A%D = B%D + C%D
from collections import deque

moves = [(0,1),(1,0)]

from collections import deque
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    def bfs(start):
        q=deque([start])
        visited = [[False] * (m+1) for _ in range(n+1)]
        visited[1][1]=True
        while q:
            now_y,now_x = q.popleft()
            
            if [now_x,now_y] in puddles:
                continue
            for move in moves:
                update_x,update_y = now_x-move[1], now_y-move[0]
                if 1<=update_x<=m and 1<=update_y<=n:
                    dp[now_y][now_x] += dp[update_y][update_x] % 1000000007
                    dp[now_y][now_x] = dp[now_y][now_x] % 1000000007
            for move in moves:
                new_y,new_x = now_y+move[0], now_x+move[1]
                if 1<=new_x<=m and 1<=new_y<=n and not visited[new_y][new_x]:
                    q.append((new_y,new_x))
                    visited[new_y][new_x]=True
                
    bfs((1,1))
    return dp[n][m]