# N-Queen
# N x N 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 0~n-1 줄마다 하나씩
# 종료조건 : 모든 퀸을 다 배치했을 때

N = int(input())

cnt = 0
lst = []
# 모든 항목을 검사시 시간초과 발생. 아래로 리스트로 공간복잡도를 올리는데신 시간 복잡도를 O(n)에서 O(1)으로 단축.
isused_row = [False] * N
# / 방향 대각선, 인덱스는 row + col
isused_cross1 = [False] * (2*N-1)  # 1 1 / 2 3 / 3 5 / 4 7 / n 2n-1
# \ 방향 대각선, 인덱스는 col - row + N - 1
isused_cross2 = [False] * (2*N-1)

def nqueen(curr):
    global cnt
    if curr == N:
        cnt += 1
        return
    else:
        for _ in range(N):
            if isused_row[_] or isused_cross1[curr+_] or isused_cross2[_-curr+N-1]:
                continue
            else:
                lst.append((curr,_))
                isused_row[_] = True
                isused_cross1[curr+_] = True
                isused_cross2[_-curr+N-1] = True
                nqueen(curr+1)
                lst.pop()
                isused_row[_] = False
                isused_cross1[curr+_] = False
                isused_cross2[_-curr+N-1] = False
        
nqueen(0)
print(cnt)