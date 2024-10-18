# 1053 ~ 1133
# 1216 ~ 1219
# dfs
# begin과 words의 각 요소를 한글자씩 비교, 같은 개수가 하나일떄 -> 변형가능, cnt+=1, begin을 word로 변경 
# 

def solution(begin, target, words):
    answer = []
    N = len(words)
    length = len(begin)
    
    if target not in words:
        return 0
    
    def dfs(in_word,cnt,visited):
        if in_word == target:
            answer.append(cnt)
            return
        else:
            for _ in range(N):
                if words[_] == in_word: continue
                match = 0
                for s in range(length):
                    if in_word[s]==words[_][s]:
                        match +=1
                
                if match == length-1 and not visited[_]:
                    visited[_] = True
                    dfs(words[_],cnt+1,visited)
                    visited[_] = False
                    
    visited = [False] * N
    dfs(begin,0,visited) 
    
    return min(answer) if answer else 0