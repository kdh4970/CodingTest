# 2108 ~ 2128
# 최소 하나의 옷
# 종류당 최대 하나
# 한 부위에서 하나를 고르거나 안 고르는 경우의 수 : 부위의 종류 + 1
# 각 부위마다 곱하여서 조합, 아무것도 안입는 공집합의 경우를 빼야함 -1
# set으로 부위 갯수 및 이름 획득
# clothes를 돌며, 부위 당 갯수 카운트

def solution(clothes):
    where = set()
    for clothe in clothes:
        where.add(clothe[1])
    where = list(where)
    items = [0]*len(where)
    for clothe in clothes:
        items[where.index(clothe[1])]+=1    
    answer = 1
    for item in items:
        answer*=item+1

    return answer-1