# 2128 ~ 2207
# 각 기능의 현재 진행률과 개발 속도가 배열로 제공
# 뒤의 기능이 먼저 개발돼도, 앞의 기능이 개발 완료될 때까지 대기 후 한번에 배포.
# 각 배포시 몇개의 기능이 배포되는지 배열로 리턴
# 가장 앞선 100이 아닌 진행도의 기능의 속도를 기반으로 잔여일 계산.
# 진행도 시뮬레이션을 진행하며, 진행도가 100퍼센트이면, 배포 대기열에 인덱스 추가.
# 예정일이 되면 배포 대기열 카운트 및 저장, 다음 배포

def get_first_idx(n,p):
    for _ in range(n):
        if p[_]!=100:
            return _
    return -1
def solution(progresses, speeds):
    answer = []
    release_until=0
    release_lst=set()
    first_idx = 0
    total = len(progresses)
    release_cnt = 0
    while True:
        if release_until==0:
            first_idx = get_first_idx(total,progresses)
            if first_idx ==-1:
                release_cnt = 0
                for i in list(release_lst):
                    if i < total:
                        release_cnt+=1
                        release_lst.remove(i)
                answer.append(release_cnt)
                break
            release_cnt = 0
            for i in list(release_lst):
                if i <first_idx:
                    release_cnt+=1
                    release_lst.remove(i)
            answer.append(release_cnt)
            release_until = (100-progresses[first_idx])//speeds[first_idx]
            release_until += 0 if (100-progresses[first_idx]) % speeds[first_idx] ==0 else 1
        for _ in range(first_idx,total):
            progresses[_]+=speeds[_]
            if progresses[_]>=100:
                progresses[_] = 100
                if _ not in release_lst:
                    release_lst.add(_)
        
        release_until -=1
            
    
    return answer[1:]