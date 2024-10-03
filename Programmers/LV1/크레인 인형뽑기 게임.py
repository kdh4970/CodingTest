### Attempt 1 : 24.10.02
### Time : 2120 ~ 2200 (40m)

### Solution
# 스택
# moves 원소 하나에 대해 스택에 담고 중복 체크 후 반복

def solution(board, moves):
    answer = 0
    stk = []
    for move in moves:
        # 위에서부터 체크
        target = None
        for _ in range(len(board)):
            if board[_][move-1]==0: continue
            else: 
                target = _
                break
        # 보드에서 지우고 스택에 삽입
        if target is not None:
            stk.append(board[target][move-1])
            board[target][move-1] = 0
        # 스택 중복 확인
            if len(stk)>=2 and stk[-1]==stk[-2]:
                stk.pop()
                stk.pop()
                answer += 2
    
    return answer