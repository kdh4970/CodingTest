#1. N*N 지도에서 가장 높은 봉우리를 찾는다.
#2. 각각의 봉우리에서부터 dfs로 등산로를 만든다.
#   단, dfs 에서 네방향 중 기존 값보다 크기가 작은 경우에만 이동이 가능하다.
#   그러나, 기존 값보다 큰 경우에 해당 높이를 깎을 수 있는 기회가 단 한번 주어진다. 최대 깎을 수 있는 깊이는 K
#   깎을 수 있는 조건은 현위치 값과 대상 위치 값의 차가 K-1 이하 인경우
#3. dfs 종료시 등산로 배열의 길이를 활용하여 최대 길이 업데이트

moves = [(-1,0),(0,1),(1,0),(0,-1)]


def find_max():
    max_val=0
    max_pos=[]
    for r in range(n):
        for c in range(n):
            if board[r][c] > max_val:
                max_val=board[r][c]
                max_pos = [(r,c)]
            elif board[r][c]==max_val:
                max_pos.append((r,c))
            else:
                continue
    return max_val, max_pos

def dfs(start):
    stk = [start]
    visited = []
    iscut=False
    while stk:
        r,c = stk.pop()
        if (r,c) in visited==1:
            continue
        visited+=[(r,c)]
        for move in moves:
            # breakpoint()
            new_r,new_c = r+move[0],c+move[1]
            if 0<=new_r<=n-1 and 0<=new_c<=n-1 and (new_r,new_c) not in visited:
                if board[r][c] > board[new_r][new_c]:
                    stk.append((new_r,new_c))
                elif 0<=(board[new_r][new_c] - board[r][c])<k and not iscut:
                    board[new_r][new_c] -= board[new_r][new_c] - board[r][c]+1
                    stk.append((new_r,new_c))
                    iscut=True

    print(visited)
    breakpoint()




T=int(input().rstrip())

for case in range(T):
    n,k=map(int,input().rstrip().split(" "))
    board = [list(map(int,input().rstrip().split(" "))) for _ in range(n)]

    val,positions = find_max()

    for top in positions:
        dfs(top)
