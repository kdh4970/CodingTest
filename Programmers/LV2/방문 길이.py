# 2058 ~ 2120

desc = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}

def solution(dirs):
    answer = 0
    now = [0,0]
    visited = set()
    for d in dirs:
        new_r,new_c = now[0] + desc[d][0], now[1] + desc[d][1]
        if -5 <= new_r <= 5 and -5 <= new_c <=5:
            if (now[0],now[1],new_r,new_c) not in visited:
                answer +=1
                visited.add((now[0],now[1],new_r,new_c))
                visited.add((new_r,new_c,now[0],now[1]))
            now[0],now[1] = new_r,new_c
        
    return answer