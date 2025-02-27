# 1546 ~ 1550

dr = [1,0,0,-1]
dc = [0,1,-1,0]


def solution(board, h, w):
    answer = 0
    target = board[h][w]
    n,m = len(board),len(board[0])
    for _ in range(4):
        new_r,new_c = h+dr[_],w+dc[_]
        if 0<=new_r<n and 0<=new_c<m and board[new_r][new_c] == target:
            answer +=1
    
    return answer