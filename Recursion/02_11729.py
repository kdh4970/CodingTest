# 하노이 탑 이동 순서
# 시간제한 1초

N = int(input())

# 한번에 하나의 원판만 이동
# 원판은 항상 아래가 작아야함.
# 위에서부터 1, 아래로 N개 원판이 있을때
# N개의 원반을 옮기기 위해, 그 위의 N-1개의 원반을 경유지에 옮겨야 함.
# 가장 큰원반이 최종 목적기둥으로 이동
# N-1개의 원반을 최종목적기둥으로 옮겨야 함.
# 종료조건 : N이 1일때, 마지막 하노이를 움직임으로써 끝.
stk = []

def move_disk(start,end):
    stk.append((start,end))

def func(n,start,end):
    hanoi(n,start,end,2)

def hanoi(n,start,end,mid):
    if n==1:
        move_disk(start,end)
    else:
        hanoi(n-1,start,mid,end)
        move_disk(start,end)
        hanoi(n-1,mid,end,start)

func(N,1,3)
print(len(stk))
for _ in stk:
    print(*_)
