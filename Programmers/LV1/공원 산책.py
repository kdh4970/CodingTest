### Attempt 1 : 24.10.03
### Time : 1614 ~ 1654 (40m)

### solution
# route 순회하며, 인덱스 에러 및 X체크 -> 스킵

def solution(park, routes):
    h,w = len(park), len(park[0])
    for r in range(h):
        for c in range(w):
            if park[r][c] == "S":
                start_r,start_c = r,c
    now=[start_r,start_c]
    
    for route in routes:
        op,n = route.split(" ")
        
        n = int(n)
        if op=="N": offset = (-n,0)
        elif op=="S": offset = (n,0)
        elif op=="W": offset = (0,-n)
        elif op=="E": offset = (0,n)
        future = [now[0]+offset[0],now[1]+offset[1]]
        if future[0]<0 or future[0]>h-1: continue
        if future[1]<0 or future[1]>w-1: continue
        step = (offset[0]//n, offset[1]//n)
        skip=False
        for _ in range(1,n+1):
            if park[now[0]+step[0]*_][now[1]+step[1]*_]=="X":
                skip=True
        if not skip: now=future
    
    return now