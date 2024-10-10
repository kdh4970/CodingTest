#1. N*N 지도에서 가장 높은 봉우리를 찾는다.
#2. 각각의 봉우리에서부터 dfs로 등산로를 만든다.
#   단, dfs 에서 네방향 중 기존 값보다 크기가 작은 경우에만 이동이 가능하다.
#   그러나, 기존 값보다 큰 경우에 해당 높이를 깎을 수 있는 기회가 단 한번 주어진다. 최대 깎을 수 있는 깊이는 K
#3. dfs 종료시 등산로 배열의 길이를 활용하여 최대 길이 업데이트


def find_max():
    for _ in








T=int(input().rstrip())

# for case in range(T):
n,k = map(int,input().rstrip().split(" "))
board = [list(map(int,input().rstrip().split(" "))) for _ in range(n)]

# print(f"#{case+1} {res}")