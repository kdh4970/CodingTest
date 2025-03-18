# 1714 ~ 1830
# 0 1 2     3 0
# 3 4 5  >> 4 1
#           5 2
# 로테이션 해서 좌로 밀기

dr = [0,1,0,1]
dc = [0,0,1,1]
new_board = []
def findnmark(r,c):
    global new_board
    val = new_board[r][c][0]
    if val ==" ":return False
    for _ in range(1,4):
        if new_board[r+dr[_]][c+dc[_]][0]==val:
            continue
        else:
            return False
    for _ in range(0,4):
        if len(new_board[r+dr[_]][c+dc[_]])==1:
            new_board[r+dr[_]][c+dc[_]]+=" "
    return True

def remove():
    for r in range(len(new_board)):
        for c in range(len(new_board[0])):
            if len(new_board[r][c])>1:
                while len(new_board[r][c])>1:
                    del new_board[r][c]
                    new_board[r].append(" ")
                continue

def solution(m, n, board):
    for r in range(n):
        t=[]
        for c in range(m-1,-1,-1):
            t.append(board[c][r])
        new_board.append(t)
    
        
    
    
    while True:
        sig = False
        for r in range(n-1):
            for c in range(m-1):
                res = findnmark(r,c)
                if res:
                    sig = True


        if sig: remove()
        else:
            break

    answer = 0
    for line in new_board:
        answer+=line.count(" ")
    return answer