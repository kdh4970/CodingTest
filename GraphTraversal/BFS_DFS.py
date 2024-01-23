
# 탐색알고리즘
# BFS, DFS

# 구현
# 1. 현재 위치를 x,y로 설정
# 2. 현재 위치에서 갈 수 있는 곳을 탐색
# 3. 갈 수 있는 곳이 있다면, 갈 수 있는 곳을 이동가능 목록에 넣음
# 4. 목록에서 하나씩 뽑아서 1~3을 반복
# 5. 목록이 비어있다면, 끝
# + 2번의 이동가능 지점 탐색시 경계선을 탐색하지 않기 위한 조건 필요 (IndexError)
# + 방문한 지점에 대해서는 다시 방문하지 않기 위한 조건 필요 (무한루프)
# + 이동가능 목록을 스택으로 구현하면 DFS, 큐로 구현하면 BFS가 됨.  
# BFS는 너비우선탐색으로, 이동가능 목록에서 가장 먼저 추가된 곳부터 탐색. 즉, 시작점과 가까운 부분부터
# DFS는 깊이우선탐색으로, 이동가능 목록에서 먼곳부터 탐색. 즉, 한 줄기를 따라 쭉

def search_and_update(map,curr,arr):
    rows = len(map)
    cols = len(map[0])
    now_r, now_c = curr

    if now_r > 0 and map[now_r-1][now_c] == 0:
        arr.append([now_r-1, now_c])
    if now_r < rows-1 and map[now_r+1][now_c] == 0:
        arr.append([now_r+1, now_c])
    if now_c > 0 and map[now_r][now_c-1] == 0:
        arr.append([now_r, now_c-1])
    if now_c < cols-1 and map[now_r][now_c+1] == 0:
        arr.append([now_r,now_c+1])

    return arr


def DFS(map:list, start, end):
    can_go = [start]
    while can_go:
        curr = can_go.pop(-1)
        map[curr[0]][curr[1]] = -1
        can_go = search_and_update(map,curr,can_go)
        print(can_go)
        
        if end and end in can_go:
            print(map)
            break



def main():
    testmap = [
        [0,1,1,1,1],
        [0,0,1,1,1],
        [1,0,0,0,1],
        [0,0,1,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0]
    ]
    print("start DFS")
    DFS(map = testmap, start=[0,0] ,end=[5,4])
    


