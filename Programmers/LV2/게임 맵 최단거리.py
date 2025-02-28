# 1705 ~ 1735
from collections import deque
dr = [0,1,-1,0]
dc = [1,0,0,-1]

def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    
    def bfs(start_point):
        q = deque([start_point])
        dist = [[0] * m for _ in range(n)]
        dist[0][0]=1
        while q:
            now = q.popleft()
            if now[0]==n-1 and now[1] ==m-1:
                return dist[n-1][m-1]
            for _ in range(4):
                new_r,new_c = now[0]+dr[_], now[1]+dc[_]
                if 0<=new_r<n and 0<=new_c<m and maps[new_r][new_c] == 1:
                    maps[new_r][new_c] = 0
                    q.append([new_r,new_c])
                    dist[new_r][new_c] = dist[now[0]][now[1]]+1
                    
        return -1
    answer = bfs((0,0))
    
            
    return answer