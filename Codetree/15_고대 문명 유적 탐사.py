# 1401 ~ 1430 문제 분석 및 솔루션 도출 (29m)
# 1430 ~ 1525 탐사 구현 (55m)
# 1531 ~ 1636 획득 구현 및 디버깅 (65m)
# total (2h 29m)



# 5x5 격자의 각 칸에는 유물조각이 배치됨.(1~7)

# 1. 탐사
# 격자내 3X3을 선택하여 회전 가능(시계방향 90, 180, 270도 중 택일, 회전 필수)
# 회전순위
#   1. 유물1차 획득 가치 최대화
#   2. 회전한 각도가 가장 작은
#   3. 회전 중심 좌표의 열이 가장 작은 구간
#   4. 회전 중심 좌표의 행이 가장 작은 구간
## 회전 함수
## old index set에서 val저장. old index set에 2를 더한 자리에 val 기입.
## r-1,c-1   r-1,c   r-1,c+1
## r,c-1      r,c     r,c+1
## r+1,c-1   r+1,c   r+1,c+1
## 맵 전체에서 유물을 찾고 획득가치를 계산하는 함수(bfs,visited) 
## 유물을 찾은경우, 가치가 max인 시점의 회전중심과 각도, 유물목록 저장.
# virtue_max,rotate_min,c_min,r_min

# 2. 유물 1차 획득
# 상하좌우 인접한 같은 종류의 유물조각은 서로 연결(bfs)
# 조각들이 세개 이상 연결괸 경우, 조각 -> 유물화, 지도상에서 삭제
# 유물의 가치는 조각 개수와 같음. (1~7은 id)
# 빈칸 채우기 + 유물 2차 획득
# 빈 공간에 유적 벽면의 숫자가 순서대로 배치됨.(열번호 작은순, 행번호 큰 순, 이전 사용된 인덱스 이후부터)
#  다시 세칸 이상이면 유물 획득
## 유물목록의 좌표를 열,행 순 정렬
## 유적벽면 숫자는 따로 기억하며, 벽면숫자에서 위의 정렬좌표에 새로 기입
## 유물획득 가치는 1에서 초깃값, 2에서는 누적
## 새로 기입후 다시 bfs 수행

### 종료조건
# 1 에서 모든회전을 해도 유물 불가시 전탐사 종료

# 3. 탐사 반복
# K번의 탐사.
# 탐사는 1~2까지가 1턴. 중간에 어떠한 방법으로도 유물 획득이 불가하다면 탐사 종료
# 
from collections import deque

K,M = map(int,input().rstrip().split(" "))
board=[list(map(int,input().rstrip().split(" "))) for _ in range(5)]
arr_M=list(map(int,input().rstrip().split(" ")))

last_M=0

dr=[-1,0,1,0]
dc=[0,1,0,-1]

dr_rotate = [-1,-1,-1,0,1,1,1,0]
dc_rotate = [-1,0,1,1,1,0,-1,-1]
## r-1,c-1   r-1,c   r-1,c+1
## r,c-1      r,c     r,c+1
## r+1,c-1   r+1,c   r+1,c+1
#1. 탐사

def rotate_board(r,c):
    global board
    val=[]
    for _ in range(8):
        idx_r=r+dr_rotate[_]
        idx_c=c+dc_rotate[_]
        val.append(board[idx_r][idx_c])
    val=deque(val)
    val.rotate(2)
    for _ in range(8):
        idx_r=r+dr_rotate[_]
        idx_c=c+dc_rotate[_]
        board[idx_r][idx_c]=val[_]

def find():
    visited=[[False]*5 for _ in range(5)]
    relic_place=[]
    relic_virtues=0
    valid_relic=[]
    for r in range(5):
        for c in range(5):
            if visited[r][c]:
                continue
            q=deque([(r,c)])
            relic_id=board[r][c]
            relic_virtue=0
            temp=[]
            while q:
                now_r,now_c = q.popleft()
                if visited[now_r][now_c]:
                    continue
                visited[now_r][now_c]=True
                relic_virtue+=1
                temp.append((now_r,now_c))
                for _ in range(4):
                    scan_r = now_r+dr[_]
                    scan_c = now_c+dc[_]
                    if not (0<=scan_r<=4) or not (0<=scan_c<=4) or visited[scan_r][scan_c] or board[scan_r][scan_c] != relic_id:
                        continue
                    q.append((scan_r,scan_c))
            if relic_virtue >=3:
                relic_virtues+=relic_virtue
                for _ in temp:
                    valid_relic.append(_)
            
    return relic_virtues,valid_relic

def scan():
    scan_res=[]
    relic_res=[]
    for r in range(1,4):
        for c in range(1,4):
            for _ in range(3):
                rotate_board(r,c)
                virtue,places=find()
                if virtue<3:
                    continue
                if not scan_res:
                    scan_res=[virtue,_,c,r]
                    relic_res=places
                else:
                    if scan_res[0]<virtue:
                        scan_res=[virtue,_,c,r]
                        relic_res=places
                    elif scan_res[0]==virtue:
                        if _ < scan_res[1]:
                            scan_res[1]=_
                            scan_res[2]=c
                            scan_res[3]=r
                            relic_res=places
                        elif _ == scan_res[1]:
                            if c<scan_res[2]:
                                scan_res[2]=c
                                scan_res[3]=r
                                relic_res=places
                            elif c==scan_res[2]:
                                if r< scan_res[3]:
                                    scan_res[3]=r
                                    relic_res=places
            rotate_board(r,c)
    # print(scan_res)
    # print(relic_res)
    return scan_res,relic_res

def get(res,relics):
    global last_M,board
    ans=res[0]
    while True:
        relics.sort(key=lambda x:x[0],reverse=True)
        relics.sort(key=lambda x:x[1])
        # print(relics)
        # for line in board:
        #     print(line)
        for relic in relics:
            board[relic[0]][relic[1]]=arr_M[last_M]
            last_M = last_M+1 if last_M<M-1 else 0
        # for line in board:
        #     print(line)
        # print("============")
        virtue,relics=find()
        if virtue<3:
            break
        ans+=virtue
    return ans

for turn in range(K):
    res,relics=scan()
    if not res or res[0]<3:
        break
    for _ in range(res[1]+1):
        rotate_board(res[3],res[2])
    final=get(res,relics)
    if final==0:break
    print(final,end=" ")
