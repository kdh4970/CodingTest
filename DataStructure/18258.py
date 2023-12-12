# 큐2

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

cmd_num = int(input())
queue = deque()
for x in range(cmd_num):
    cmd = input().split(" ")
    if cmd[0] == "push": queue.append(int(cmd[1])); continue
    elif cmd[0] == "pop": 
        if len(queue) != 0 : print(queue[0]);queue.popleft(); continue
        else: print("-1"); continue
    elif cmd[0] == "size": print(len(queue)); continue
    elif cmd[0] == "empty":
        if len(queue) == 0: print("1"); continue
        else: print("0"); continue
    elif cmd[0] == "front":
        if len(queue) == 0: print("-1"); continue
        else: print(queue[0]); continue
    elif cmd[0] == "back":
        if len(queue) == 0: print("-1"); continue
        else: print(queue[-1]); continue


