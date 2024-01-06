# 그림
# stack 기반 dfs

import sys
def input():
    return sys.stdin.readline().rstrip()


def search_and_update(position,arr,pic):
    h,w = len(pic), len(pic[0])
    now_x, now_y = position[0],position[1]
    if pic[max(now_x-1,0)][now_y] == 1:
        arr.append([max(now_x-1,0), now_y])
    if pic[now_x][max(now_y-1,0)] == 1:
        arr.append([now_x,max(now_y-1,0)])
    if pic[min(now_x+1,h-1)][now_y] == 1:
        arr.append([min(now_x+1,h-1), now_y])
    if pic[now_x][min(now_y+1,w-1)] == 1:
        arr.append([now_x,min(now_y+1,w-1)])
    return arr

def calc_space(start,pic):
    stk = [start]
    space = 0
    while len(stk) != 0:
        curr_pos = stk.pop()
        if pic[curr_pos[0]][curr_pos[1]] == 1:
            pic[curr_pos[0]][curr_pos[1]] = -1
            space += 1
        stk = search_and_update(curr_pos,stk,pic)
    return space, pic


HEIGHT, WIDTH = list(map(int,input().split()))
image = []

for _ in range(HEIGHT):
    image.append(list(map(int,input().split())))

res = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        startPoint = [y,x]
        if image[y][x] != 1: continue 
        space, image = calc_space(startPoint,image)
        res.append(space)


print(len(res))
print(max(res) if res else 0)