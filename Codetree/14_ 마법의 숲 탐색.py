# 1550 ~ 1627 솔루션 구상
# 1654 ~ 1740 구현

# 지도의 기본값은 0, 정령의 위치는 1, 골렘의 위치는 2, 골렘 출구는 3으로 가정한다.
# 남하가 완료된 골렘의 위치는 남하 순으로 갯수 *-1  고정 출구는 배열에 저장
# 현재 정령의 위치 출구를 저장
# 출구 인덱스 0123은 북동남서

#1. 정령은 십자모양 골렘의 정중앙에 있으며, 골렘은 남쪽으로 이동한다.(단 아래 세칸이 빈 경우)
## 정령의 현 위치 기반으로 좌,우,아래 좌표에서 각각 아래쪽이 비었는지 확인한다.
## 빈 경우, 현 정령 및 골렘 위치를 지우고, 정령 및 출구 값을 업데이트하고 지도에 반영한다.

#2. 1이 불가한 경우, 서쪽으로 회전하며 한칸 내려간다. 출구가 반시계 회전 (서쪽 세칸이 비었고, 그 아래 두칸이 빈경우) 
## 정령의 현 위치 기반으로 상,하,좌 좌표에서 각각 서쪽이 비었는지 확인한다.
## 빈 경우, 현 정령 및 골렘 위치를 지우고, 정령 및 출구 값을 업데이트하고 지도에 반영한다.

#3. 2가 불가한 경우, 동쪽으로 회전하며 한칸 내려간다. 출구가 시계 회전 (동쪽 세칸이 비었고, 그 아래 두칸이 빈경우)
## 정령의 현 위치 기반으로 상,하,우 좌표에서 각각 동쪽이 비었는지 확인한다.
## 빈 경우, 현 정령 및 골렘 위치를 지우고, 정령 및 출구 값을 업데이트하고 지도에 반영한다.

#4. 위 과정을 반복하여 골렘이 최대한 남하한 경우, 골렘 내부에서 정령이 남하한다. (단, 골렘 출구가 다른 골렘과 인접하면 넘어 갈 수 있다.)
## 이후 해당 위치가 출구이고, 인접 삼면 중 골렘이 존재하면 다시 이동이 가능하다.
## visited배열을 만든다.
## 정령위치에서 탐색을 수행한다. 단, 기본적으로 한 골렘(-2 or -3... etc)에서 탐색하며, 출구(-1)를 발견하면 해당 위치중 인접한 골렘이동이 가능하다.
## 인접 골렘 이동 시 해당 인덱스를 기반으로 해당 골렘을 계속 서치 가능하다.
## 순간순간 max row 값을 갱신한다. 

#5. 정령의 남하가 끝나면, 해당 행수를 누적한다.
#6. 골렘이 숲을 초과하면, 해당 골렘을 포함하여 이전 골렘들을 모두 지우고, 다음 골렘을 투입한다.
## 현재 골렘의 아래부분 0,c가 비어있는가?
## (0,c-1), (0,c+1), (1,c)가 비어있는가?
## 아니라면 서쪽아래를 체크, 

R,C,K=map(int,input().rstrip().split(" "))
forest = [[0]*C for _ in range(R)]
golems = [list(map(int,input().rstrip().split(" ")) for _ in range(K)]

dgolem=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
ddown=[(2,0),(1,-1),(1,1)]
dleft=[(0,-2),(-1,-1),(1,-1)]
dright=[(0,2),(-1,1),(1,1)]
fixed_golem_cnt = 0

exit_arr=[]

def go_spirit(now_r,now_c):


def go_down(r,c,exit_dir):
    if r==R-2:
        global fixed_golem_cnt,exit_arr
        # 4번 로직
        ## 골렘 픽스 및 출구 배열 저장
        fixed_golem_cnt += 1
        for _ in range(5):
            dr,dc = dgolem[_]
            forest[r+dr][c+dc]=fixed_golem_cnt*(-1)
        exit_r=r+dgolem[exit_dir+1][0]
        exit_c=c+dgolem[exit_dir+1][1]
        exit_arr.append((exit_r,exit_c))
        ## 정령 남하


    if r==-2:
        if forest[r+ddown[0][0]][c+ddown[0][1]]==0:
            r+=1
            go_down(r,c,exit_dir)
        else:
            return -1 # 내려갈 수 없음
    # 1번 로직 시도
    for _ in range(3):
        dr,dc = ddown[_]
        if 0 <= r+dr <= R-1 and 0 <= c+dc <= C-1 and forest[r+dr][c+dc]!=0:
            break
        if _==2:
            r+=1
            go_down(r,c,exit_dir)
    # 2번 로직 시도
    for _ in range(3):
        dr,dc = dleft[_]
        if 0 <= r+dr <= R-1 and 0 <= c+dc <= C-1 and forest[r+dr][c+dc]!=0:
            break
        if _==2:
            c-=1
            exit_dir-=1 if exit_dir >1 else 3
            go_down(r,c,exit_dir)
    # 3번 로직 시도
    for _ in range(3):
        dr,dc = dright[_]
        if 0 <= r+dr <= R-1 and 0 <= c+dc <= C-1 and forest[r+dr][c+dc]!=0:
            break
        if _==2:
            c+=1
            exit_dir+=1 if exit_dir <3 else 0
            go_down(r,c,exit_dir)


for golem in golems:
    start_col,exit_dir = golem

    ## 못 내려갈 때 까지 남하
    go_down(-2,start_col-1,exit_dir)
        