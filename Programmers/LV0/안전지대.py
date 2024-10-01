### Attempt 1 : 24.10.02
### Time : 0020 ~ 0039 (19m)

### Solution
# 지뢰 1 지도를 지뢰1 위험2로 작성 후 0 카운트

def solution(board):
    answer = 0
    size = len(board)
    cnt = 0
    for r in range(size):
        for c in range(size):
            if board[r][c]==1:
                print(r,c)
                if r>0 and c>0:
                    board[r-1][c-1] = 2 if board[r-1][c-1] !=1 else 1
                if r>0 and c<size-1:
                    board[r-1][c+1] = 2 if board[r-1][c+1] !=1 else 1
                if r<size-1 and c>0:
                    board[r+1][c-1] = 2 if board[r+1][c-1] !=1 else 1
                if r<size-1 and c<size-1:
                    board[r+1][c+1] = 2 if board[r+1][c+1] !=1 else 1
                if r>0:
                    board[r-1][c] = 2 if board[r-1][c] !=1 else 1
                if c>0:
                    board[r][c-1] = 2 if board[r][c-1] !=1 else 1
                if r<size-1:
                    board[r+1][c] = 2 if board[r+1][c] !=1 else 1
                if c<size-1:
                    board[r][c+1] = 2 if board[r][c+1] !=1 else 1
    
    for r in range(size):
        for c in range(size):
            answer += 1 if board[r][c]==0 else 0
    
    return answer