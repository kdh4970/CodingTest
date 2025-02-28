# 1636 ~ 1704

# 1차 풀이 : 시간초과
# def solution(topping):
#     answer = 0
#     set_topping = set(topping)
#     categories = len(set_topping)
#     for _ in range(1,len(topping)-1):
#         if len(set(topping[:_])) == len(set(topping[_:])):
#             answer +=1    
#     return answer

# 2차 풀이

def solution(topping):
    answer = 0
    left = {}
    right = {}
    
    # 전체를 오른쪽에 주고 하나씩 왼쪽으로 옮기며 체크
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
    
    for t in topping:
        if len(left) == len(right):
            answer += 1
        
        if t in left:
            left[t] += 1
        else:
            left[t] = 1
        
        right[t] -= 1
        if not right[t]:
            del right[t]
        
    return answer
        
        
        
    
    