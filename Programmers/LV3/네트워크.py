# 1241 ~ 1358

# 1101 #01 03
# 1101 #13
# 0010
# 1101
# 배열의 삼각형 내의 좌표들을 순회하며, dfs로 방문한 지점 visited 마킹
# 방문 중 동일한 네트워크 내면 은 계속 해서 dfs 수행



def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(i):
        visited[i] = True
        for _ in range(n):
            if computers[i][_]==1 and not visited[_]:
                dfs(_)
    
    for _ in range(n):
        if not visited[_]:
            dfs(_)
            answer +=1
    return answer