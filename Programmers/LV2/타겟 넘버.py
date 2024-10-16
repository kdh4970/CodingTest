# 1725 ~ 1745
# 


answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(idx,val):
        global answer
        if idx == n and val==target:
            answer +=1
        elif idx<n:
            dfs(idx+1,val+numbers[idx])
            dfs(idx+1,val-numbers[idx])
            
    dfs(0,0)
    
    return answer