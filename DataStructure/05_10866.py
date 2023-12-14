# 덱

import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

def push_front(q,x): q.appendleft(x)
def push_back(q,x): q.append(x)
def pop_front(q): 
    if len(q):
        print(q[0]) 
        q.popleft()
    else:
        print(-1)
def pop_back(q):
    if len(q):
        print(q[-1])
        q.pop()
    else:
        print(-1)
def size(q): print(len(q))
def empty(q): print(0) if len(q) else print(1)
def front(q): print(q[0]) if len(q) else print(-1)
def back(q): print(q[-1]) if len(q) else print(-1)

N = int(input())
q = deque()
for _ in range(N):
    i = input()
    cmd = i.split()
    if cmd[0]=="push_back": push_back(q,int(cmd[1]))
    elif cmd[0]=="push_front": push_front(q,int(cmd[1]))
    elif cmd[0]=="pop_front": pop_front(q)
    elif cmd[0]=="pop_back": pop_back(q)
    elif cmd[0]=="size": size(q)
    elif cmd[0]=="empty": empty(q)
    elif cmd[0]=="front": front(q)
    elif cmd[0]=="back": back(q)
    
    