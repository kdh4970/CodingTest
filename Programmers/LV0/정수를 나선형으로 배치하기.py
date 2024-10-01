### Attempt 1 : 24.10.01
### Time : 2230 ~ 2300 (30m)

### Solution
# 현재 인덱스에서 현재 방향 만큼 더한 자리에 값 할당
# 범위 초과시 또는 이미 값이 있는경우 방향 전환

def solution(n):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    answer = [[-1]*n for _ in range(n)]
    def is_turn(now_dir,now_r,now_c):
        if now_dir==directions[0] and (now_c == n-1 or answer[now_r+now_dir[0]][now_c+now_dir[1]]!=-1):
            return True
        elif now_dir==directions[1] and (now_r == n-1 or answer[now_r+now_dir[0]][now_c+now_dir[1]]!=-1):
            return True
        elif now_dir==directions[2] and (now_c == 0 or answer[now_r+now_dir[0]][now_c+now_dir[1]]!=-1):
            return True
        elif now_dir==directions[3] and (now_r == 0 or answer[now_r+now_dir[0]][now_c+now_dir[1]]!=-1):
            return True
        else:
            return False
    curr_dir_idx = 0
    curr_dir = directions[curr_dir_idx]
    now_r,now_c = 0,0
    answer[now_r][now_c] = 1
    
    for _ in range(2,1+n**2):
        if is_turn(curr_dir,now_r,now_c):
            curr_dir_idx = curr_dir_idx+1 if curr_dir_idx< len(directions)-1 else 0
            curr_dir = directions[curr_dir_idx]
        now_r+=curr_dir[0]
        now_c+=curr_dir[1]
        answer[now_r][now_c] = _
    
    return answer