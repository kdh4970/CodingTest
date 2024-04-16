# 종이의 개수 - 분할정복
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
result = [0,0,0]
def check(size,start):
    base_num = board[start[0]][start[1]]
    for r in range(size):
        for c in range(size):
            if board[start[0]+r][start[1]+c] != base_num:
                return False
    return True
def func(size,start):
    r,c = start
    if size == 1: 
        result[board[r][c]] += 1
        return
    if check(size,start):
        result[board[r][c]] += 1
        return
    crop_size = size//3
    func(crop_size,(r,c))
    func(crop_size,(r+crop_size,c))
    func(crop_size,(r+2*crop_size,c))
    func(crop_size,(r,c+crop_size))
    func(crop_size,(r+crop_size,c+crop_size))
    func(crop_size,(r+2*crop_size,c+crop_size))
    func(crop_size,(r,c+2*crop_size))
    func(crop_size,(r+crop_size,c+2*crop_size))
    func(crop_size,(r+2*crop_size,c+2*crop_size))
func(N,(0,0))
print(result[-1])
print(result[0])
print(result[1])