# 1625 ~ 1712
# 현재 피로도 K에 대해, 최소 필요 피로도 및 소모 피로도가 배열로 주어짐.
# 유저가 탐험 할 수 있는 최대 던전 수.

answer = 0
def solution(k, dungeons):
    n=len(dungeons)
    v=[False]*n
    
    def dfs(cnt,fatigue,arr,visited):
        global answer
        if cnt > answer:
            answer = cnt
        for _ in range(n):
            if not visited[_] and fatigue>=dungeons[_][0]:
                visited[_]=True
                dfs(cnt+1,fatigue-dungeons[_][1],arr+[_],visited)
                visited[_]=False
            
    dfs(0,k,[],v)
    
    
    return answer