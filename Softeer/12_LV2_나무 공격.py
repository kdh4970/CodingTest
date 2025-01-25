import sys


n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
attacks = [list(map(int,input().split())) for _ in range(2)]

for attack in attacks:
    for line in range(attack[0]-1,attack[1]):
        for col in range(m):
            if board[line][col]==1:
                board[line][col]=0
                break
result = 0
for line in board:
    result += sum(line)
print(result)
        