# 색종이 만들기 - 분할정복
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
result = [0,0] # 0 = white, 1 = blue 

def check(size,pos):
    r,c = pos
    base_num = board[r][c]
    for dr in range(size):
        for dc in range(size):
            if board[r+dr][c+dc]!=base_num:
                return False
    return True

def crop(size,pos):
    r,c = pos
    if size == 1 or check(size,pos):
        result[board[r][c]] += 1
        return
    crop_size = size // 2
    crop(crop_size,(r,c))
    crop(crop_size,(r+crop_size,c))
    crop(crop_size,(r,c+crop_size))
    crop(crop_size,(r+crop_size,c+crop_size))
    
crop(N,(0,0))
print(result[0])
print(result[1])