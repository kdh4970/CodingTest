# 폴리오미노

import sys
def input():
    return sys.stdin.readline().rstrip()

board = input()
size = len(board)
res = board.replace("XXXX","AAAA")
res = res.replace("XX","BB")
print(res if res.find("X") == -1 else -1)