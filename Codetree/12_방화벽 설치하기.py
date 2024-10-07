# 2035 ~ 2141 (66m)
# 1. 방화벽 세개를 설치할 위치를 불과 인접한 지점들 중에서 선정 - 재귀 백트래킹
# 2. 선정된 조합마다 불을 시뮬레이션하여 남은 안전지대 수 카운트 - BFS
from collections import deque

n,m = map(int,input().rstrip().split(" "))
board = []
fires = []
firewalls = []
can_firewall= []
for r in range(n):
    line = list(map(int,input().rstrip().split(" ")))
    board.append(line)
    for c in range(m):
        if line[c]==2:
            fires.append((r,c))
        elif line[c]==1:
            firewalls.append((r,c))
        else:
            can_firewall.append((r,c))
for fire in fires:
    r,c = fire

arr=[]

def can_go(q,r,c):
    if r>0 and board[r-1][c]==0:
        board[r-1][c]=2
        q.append((r-1,c))
    if c<m-1 and board[r][c+1]==0:
        board[r][c+1]=2
        q.append((r,c+1))
    if r<n-1 and board[r+1][c]==0:
        board[r+1][c]=2
        q.append((r+1,c))
    if c>0 and board[r][c-1]==0:
        board[r][c-1]=2
        q.append((r,c-1))
    return q

def count_safe():
    res=0
    for line in board:
        res+=line.count(0)
    return res

def bfs(start):
    q=deque([start])
    while q:
        r,c = q.popleft()
        if board[r][c]==2:
            q = can_go(q,r,c)

safe = 0
def func(i):
    global safe
    if len(arr)==3:
        ## set firewall
        # print(arr)
        for _ in arr:
            r,c = can_firewall[_]
            board[r][c]=1
        ## fire simul
        for fire in fires:
            bfs(fire)

        safe = max(safe,count_safe())
            
        # ## roll back
        # if arr==[4,5,6]:
        #     for line in board:
        #         print(line)
        for r in range(n):
            for c in range(m):
                if (r,c) not in fires and (r,c) not in firewalls:
                    board[r][c]=0
    else:
        for _ in range(len(can_firewall)):
            if _>=i and _ not in arr:
                arr.append(_)
                func(_)
                arr.pop()

        
func(0)
print(safe)