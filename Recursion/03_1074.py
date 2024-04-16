# Z - 분할정복
# 시간제한 0.5초

# 2^N * 2^N 사이즈 배열을 Z로 순회하며, r행 c열이 몇번째로 탐색되는지 찾는 문제
# 종료 조건 : 현재 탐색 지점이 r행 c열인 경우
# N=1 : 2 x 2 배열을 Z 순회 
# N=2 : 4 x 4 배열을 2 x 2 배열 블럭 4개로 쪼개고, 각 블럭을 Z순회, 블럭 내에서도 Z 순회
# N=k : 2^k x 2^k 배열을 2^(k-1) x 2^(k-1) 배열 블럭 4개로 쪼개고, 각 블럭을 Z 순회


N,R,C = list(map(int,input().split()))

lst = [[]*4 for _ in range(4)]


def func(n,r,c):
    if n==0:
        return 0
    else:
        half_block = 1<<(n-1)
        if r<half_block and c<half_block:
            return func(n-1,r,c)
        elif r<half_block and c>=half_block:
            return half_block**2 + func(n-1,r,c-half_block)
        elif r>=half_block and c<half_block:
            return 2*(half_block**2) + func(n-1,r-half_block,c)
        elif r>=half_block and c>=half_block:
            return 3*(half_block**2) + func(n-1,r-half_block,c-half_block)


print(func(N,R,C))