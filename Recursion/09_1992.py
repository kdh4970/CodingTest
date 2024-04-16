# 쿼드 트리 - 분할정복
N = int(input())
image = []
res = ""

for _ in range(N):
    text = input()
    line = [int(_) for _ in text]
    image.append(line)

def check(size,pos):
    r,c = pos
    base = image[r][c]
    for dr in range(size):
        for dc in range(size):
            if image[r+dr][c+dc] != base:
                return False
    return True

def func(size,pos):
    global res
    r,c = pos
    if size == 1 or check(size,pos):
        res += str(image[r][c])
        return
    res += "("
    crop = size // 2
    func(crop,(r,c))
    func(crop,(r,c+crop))
    func(crop,(r+crop,c))
    func(crop,(r+crop,c+crop))
    res += ")"
    
func(N,(0,0))
print(res)