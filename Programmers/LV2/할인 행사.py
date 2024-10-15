# 1725 ~ 1741
# 리스트 슬라이싱은 인덱스에러가 발생하지 않도록 내부적으로 처리한다.


def solution(want, number, discount):
    answer = 0
    
    for day in range(len(discount)-9):
        d=dict()
        for i in range(len(want)):
            d[want[i]]=number[i]
        dis = discount[day:day+10]
        for item in dis:
            if item in d:
                d[item]-=1 if d[item]>0 else 0
        if sum(list(d.values())) == 0:
            answer+=1
    
    return answer