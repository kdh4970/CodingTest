# 1943 ~ 2049 솔루션 도출 + 루돌프 함수 작성(66m)
# 2102 ~ 2242 구현 (100m)
# 2250 ~ 2315 디버깅 (25m)
# total 3h 11m

# 턴제
# 루돌프 선, 1~P 산타 순차 이동(기절 or 이탈 산타는 이동 X)
 

N,M,P,C,D=map(int,input().rstrip().split(" "))
rudolph_position=list(map(lambda x:x-1,list(map(int,input().rstrip().split(" ")))))
santa_status=[0]*P
santa_scores=[0]*P
santa_position=[0]*P
for _ in range(P):
    n,r,c = map(int,input().rstrip().split(" "))
    santa_position[n-1]=[r-1,c-1]
# print(santa_position)

def print_positions():
    arr=[[-1]*5 for _ in range(5)]
    arr[rudolph_position[0]][rudolph_position[1]]="R"
    for s in range(P):
        if santa_status[s]!=-1:
            arr[santa_position[s][0]][santa_position[s][1]]=s
    for line in arr:
        print(line)

def collision_santas(r,c,santa_id,direction,attacker):
    if attacker=="santa":
        new_r = r-(dr_santa[direction])
        new_c = c-(dc_santa[direction])
    elif attacker=="rudolph":
        new_r = r+(dr_rudolph[direction])
        new_c = c+(dc_rudolph[direction])
    santa_position[santa_id]=[new_r,new_c]
    # print(f"Santa {santa_id} moved to {new_r},{new_c} by collision")
    if not (0<=new_r<=N-1) or not (0<=new_c<=N-1):
        santa_status[santa_id]=-1
        santa_position[santa_id]=[-1,-1]
        # print(f"Santa {santa_id} is dead.")
        return
    for _ in range(P):
        if [new_r,new_c] == santa_position[_] and santa_id != _:
            collision_santas(new_r,new_c,_,direction,attacker)
            return
    
    

# 루돌프
# 가장 가까운 탈락하지 않은 산타로 1칸 돌진
# 거리는 (r2-r1)^2+(c2-c1)^2
# 가장 가까운 산타가 여럿이면, r이 큰산타에게 돌진
# r이 동일한 경우 c가 큰 기절하지 않은 산타에게 돌진 >> 산타 상태 0인 경우만
# 상하좌우 대각선 총 8방향 이동 가능. 가장 우선순위 높은 산타에게 가장 가까워지는 방향으로 돌진
# 1. 모든 산타와의 거리계산, 최단거리 산타들의 인덱스 저장.
# 2. 최단거리 산타들 중 조건에 따라 산타 선정
# 3. 행, 열 체크 동일 시 해당방향이동
# 4. 사분면 체크, 해당방향들에서 각각 거리계산 하여 최적점 선정
dr_rudolph=[1, 1, 0, -1, -1, -1, 0, 1]
dc_rudolph=[0, 1, 1, 1, 0, -1, -1, -1]

def go_rudolph():
    global rudolph_position
    distances=[]
    for _ in range(P):
        if santa_status[_]>=0:
            distances.append((rudolph_position[0] - santa_position[_][0])**2 + (rudolph_position[1] - santa_position[_][1])**2)
        else: distances.append(1e5)
    # print(distances)
    
    min_dist=min(distances)
    if min_dist==1e5:return
    nearst_santa=[(x,santa_position[x]) for x in range(P) if distances[x]==min_dist]
    # print(nearst_santa)

    nearst_santa.sort(key=lambda x:(x[1][0],x[1][1]),reverse=True)
    # print(nearst_santa)

    target_santa= nearst_santa[0] # idx,(r,c)
    nearst_dir=-1
    for _ in range(8):
        new_r=rudolph_position[0]+dr_rudolph[_]
        new_c=rudolph_position[1]+dc_rudolph[_]
        dist = (new_r - target_santa[1][0])**2 + (new_c - target_santa[1][1])**2
        if dist>= min_dist:
            continue
        else:
            min_dist=dist
            nearst_dir=_
    if nearst_dir==-1:
        return
    rudolph_position[0]+=dr_rudolph[nearst_dir]
    rudolph_position[1]+=dc_rudolph[nearst_dir]
    # print(f"Rudolph moved to {rudolph_position}")

    if rudolph_position in santa_position:
        santa = santa_position.index(rudolph_position)
        # print(f"Rudolph hit the Santa {santa}")
        santa_status[santa]=2
        santa_scores[santa]+=C
        new_r = santa_position[santa][0]+(C*dr_rudolph[nearst_dir])
        new_c = santa_position[santa][1]+(C*dc_rudolph[nearst_dir])
        santa_position[santa]=[new_r,new_c]
        # print(f"Santa {santa} moved to {new_r},{new_c} by collision")
        if not (0<=new_r<=N-1) or not (0<=new_c<=N-1):
            santa_status[santa]=-1
            santa_position[santa]=[-1,-1]
            # print(f"Santa {santa} is dead.")
            return
        for _ in range(P):
            if _!=santa and santa_position[_]==santa_position[santa]:
                collision_santas(new_r,new_c,_,nearst_dir,"rudolph")
                
    

# 산타
# 루돌프에게 가까워지는 방향으로 1칸 이동
# 1. 사방향 탐색, 비어있는지 체크
# 2. 비어있다면, 이동시 거리가 단축되는지 체크
# 3. 단축된다면, 이동
# 4. 단축되지 않으면 홀드
# 산타 겹치기 or 이탈 불가
# 이동 불가시 홀드
# 이동 가능해도 현재보다 가까워지지 않는다면 홀드
# 상하좌우 4방향 이동가능, 여러방향 동일한 경우, 상우하좌 우선순위
dr_santa=[-1, 0, 1,0]
dc_santa=[0, 1, 0,-1]



def go_santa():
    for santa in range(P):
        if santa_status[santa]==-1 or santa_status[santa]>0:
            continue
        origin_dist = (rudolph_position[0]-santa_position[santa][0])**2 + (rudolph_position[1]-santa_position[santa][1])**2
        min_dist=1e5
        nearst_dir=-1
        for _ in range(4):
            new_r = santa_position[santa][0]+dr_santa[_]
            new_c = santa_position[santa][1]+dc_santa[_]
            if [new_r,new_c] not in santa_position:
                dist = (rudolph_position[0]-new_r)**2 + (rudolph_position[1]-new_c)**2
                if origin_dist>dist and min_dist>dist:
                    min_dist=dist
                    nearst_dir=_
        # print(f"Santa {santa} moved from {santa_position[santa]}")
        # print(f"Rudolph is {rudolph_position}")
        if nearst_dir!=-1:
            santa_position[santa][0]+=dr_santa[nearst_dir]
            santa_position[santa][1]+=dc_santa[nearst_dir]
            # print(f"Santa {santa} moved to {santa_position[santa]}")
        # else:
            # print(f"Santa {santa} failed to move")
        if santa_position[santa]==rudolph_position:
            # print(f"Santa {santa} hit the Rudolph")
            santa_status[santa]=2
            santa_scores[santa]+=D
            new_r = santa_position[santa][0]-(D*dr_santa[nearst_dir])
            new_c = santa_position[santa][1]-(D*dc_santa[nearst_dir])
            santa_position[santa]=[new_r,new_c]
            # print(f"Santa {santa} moved to {santa_position[santa]} by collision")
            if not (0<=new_r<=N-1) or not (0<=new_c<=N-1):
                santa_status[santa]=-1
                santa_position[santa]=[-1,-1]
                # print(f"Santa {santa} is dead.")
                continue
            for _ in range(P):
                if _!=santa and santa_position[_]==santa_position[santa]:
                    collision_santas(new_r,new_c,_,nearst_dir,"santa")
                

# 충돌
# 조건 : 산타와 루돌프 같은칸 
# 루돌프가 돌진한 경우 : 산타 점수 C획득, 루돌프가 온 반대방향으로 C만큼 밀려남
# 산타가 돌진한 경우 : 산타 점수 D감점, 자신이 이동한 반대로 D만큼 밀려남
# 밀려남은 순간이동이라고 간주
# 밀린 위치가 게임판 밖이면 탈락
# 다른 산타가 이미 있는경우 상호작용

# 상호작용
# 기존의 산타는 산타가 날아온 방향 반대로 한칸 밀림
# 그 옆에 산타가 있으면 연쇄, 이탈시 탈락

# 기절
# 산타는 루돌프와 충돌 후 밀리고 기절. k턴 충돌시 k+2턴부터 이동가능
# 기절 산타는 자의적인 이동만 불가능
# 루돌프는 기절산타에게 돌진하지 않음

## 충돌 체크
## 루돌프 차례에 충돌시 : 산타 가산점, 산타 해당 방향 C만큼 이동
## 이동한 자리 중복 체크 : 중복시 연쇄이동
## 산타 차례에 충동시 : 산타 감점, D만큼 밀려남
## 충돌 후 산타 상태를 기절로
## 산타 상태는 -1 탈락 0 정상, 1이상 기절상태, 매턴 시작시 1보다 큰 산타 값-1
## 충돌시 +2


# 게임종료
# M턴에 걸쳐 루돌프 산타가 이동을 마친경우 or 모든 산타가 탈락한 경우
# 생존 산타는 한턴 끝날때마다 +1점


for turn in range(M):
    go_rudolph()
    # print_positions()
    go_santa()
    # print_positions()
    for _ in range(P):
        if santa_status[_] !=-1:
            santa_scores[_] +=1
        if santa_status[_] >0:
            santa_status[_]-=1
    if sum(santa_status)==(-1)*P:
        break

print(*santa_scores)