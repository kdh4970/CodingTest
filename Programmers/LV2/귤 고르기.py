# 1357 ~ 1453

# tangerine에서 K개를 뽑는데, 뽑은 귤의 종류가 최소가 되도록, 즉 중복이 많도록
# 각 배열에서 고유 원소와 카운트를 저장
# 카운트 기준 정렬
# 딕셔너리 아이템 정렬

def solution(k, tangerine):
    answer = 0
    unique=set(tangerine)
    freqs=dict()
    
    for t in tangerine:
        if t not in freqs:
            freqs[t]=1
        else:
            freqs[t]+=1
    
    sortedT=sorted(freqs.items(),key=lambda x:x[1],reverse=True)
    total=0
    for _ in range(len(sortedT)):
        total+=sortedT[_][1]
        if total >=k:
            answer = _ +1
            break
        else:
            continue
    # print(max_val)
    # print(freqs)
    
    
    return answer