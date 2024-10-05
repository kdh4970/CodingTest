### Attempt 1 : 24.10.05
### Time : 1656 ~ 1702 (6m)

def solution(arr):
    answer = 0
    
    while True:
        answer+=1
        condition=True
        for _ in arr:
            if answer % _ > 0:
                condition=False
                break
        if condition:
            break
    
    return answer