### Attempt 1 : 24.10.01
### Time : 2311 ~ 2414 (63m)

### Solution
# 반복 : 가장 낮은 start ~ 가장 높은 end
# 측정 미시작이고, 중복이 2이상인가? -> 중복에서 현위치가 종점인 갯수를 빼도 2 이상인가? -> 측정 시작
# 측정 중
#  마지막 -> 종료
#  중복이고, 중복에서 현위치가 종점인 갯수를 뺐을때 2미만인가?(다음에 연결안되는지) ->종료

def solution(lines):
    answer = 0
    start,end = 100,-100
    for _ in lines:
        if start>_[0]:
            start = _[0]
        if end<_[1]:
            end = _[1]
    endchk = [x[1] for x in lines]
    stacked=-200
    
    for _ in range(start,end-start+1):
        count = 0
        endcnt = 0
        for line in lines:
            if line[0]<= _ <=line[1]:
                count+=1
                if _==line[1]: endcnt+=1
        
        print(_,count,endcnt,stacked,answer)  
        if stacked == -200 and (count>=2 and count-endcnt>=2) :
            stacked = _
            continue
        if stacked !=-200 and (count>=2 and count-endcnt<2):
            answer += abs(_-stacked)
            stacked = -200
            continue
        if _== end-start and stacked != -200:
            answer += abs(_-stacked)
                
                
    return answer
