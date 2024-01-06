# 탐색알고리즘
# !! 나중에 그래프 공부하고 다시 볼것.

# 1. array[0] 확인해서 그 위치로 이동하고, array[0] 삭제, 도착지점 -1 표시
# 2. 현 위치에서 이동가능지점 확인하여 array 저장
# 3. 1번으로 돌아감.

# 여기서 목적지까지 도착여부를 확인하려면. 아래사항 추가해야 함.
# 1번을 수행 하기 전 array 가 비어있다면, 더이상 갈 수 있는곳이 없다는 것이므로 return False
# 2번을 수행하는 중 이동가능지점에 목적지가 포함되어 있다면 갈 수 있으므로 return True


# 이 함수는 현 위치에서 지도상 4방향을 탐색하여 이동가능여부 확인 및 arr에 저장.
# 테두리에서 IndexError를 피하기 위하여 min,max 함수를 사용함.
# 0,0은 시작점임과 동시에 최초에 값을 -1로 지정.
# 따라서 min max로 인덱스 에러가 나는 테두리 위치 중 현위치는 이미 값이 -1 이며, min max 값의 결과는 현 위치를 가르키게 되어,
# -1 값으로 인해 if 조건 False가 됨.


# array[0]을 뽑으면 BFS, array[-1]을 뽑으면 DFS 가 됨.
# 

def search_and_update(_pos,_map,_arr):
    h,w = len(_map), len(_map[0])
    now_x, now_y = _pos[0],_pos[1]
    # 왼쪽
    if _map[max(now_x-1,0)][now_y] == 0:
        _arr.append([max(now_x-1,0 ),now_y])
    # 위쪽
    if _map[now_x][max(now_y-1,0)] == 0:
        _arr.append([now_x,max(now_y-1,0)])
    # 오른쪽
    if _map[min(now_x+1,h-1)][now_y] == 0:
        _arr.append([min(now_x+1,h-1),now_y])
    # 아래쪽
    if _map[now_x][min(now_y+1,w-1)] == 0:
        _arr.append([now_x,min(now_y+1,w-1)])
    
    
    return _arr

def can_go(start, end, map_=None):
    arr = [start]

    while len(arr) != 0 :
        #1
        current_pos = arr.pop(0)
        map_[current_pos[0]][current_pos[1]] = -1

        #2.
        arr = search_and_update(current_pos,map_,arr)
        if end in arr:
            return True
    return False

map_ = [
    [0,1,1,1,1],
    [0,0,1,1,1],
    [1,0,0,0,1],
    [0,0,1,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0]
]
can_go([0,0],[5,4],map_)
    