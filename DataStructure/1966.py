# 프린터 큐
import sys
from collections import deque
from copy import deepcopy
def input():
    return sys.stdin.readline().rstrip()



N = int(input())
target = []
priority = []
for _ in range(N):
    cnt, temp_target = map(int,input().split())
    target.append(temp_target)
    priority.append(deque(map(int,input().split())))



def isHighestPriority(priority_q):
    if priority_q[0] == max(priority_q): 
        return True
    else:
        return False

for _ in range(N):
    cnt=0
    print_list=priority[_]
    while print_list is not None:
        if isHighestPriority(print_list):# 최고우선순위이면
            if target[_] == 0: # 현재 출력순번이 타겟인 경우
                print(cnt+1)
                break
            else: # 타겟이 아닌경우, 출력 후 타겟 대기열 -1
                print_list.popleft()
                target[_] -= 1
            cnt += 1
        else:# 최고 우선순위가 아니면
            if target[_] == 0: # 타겟인 경우 타겟 인덱스 가장 마지막
                target[_] = len(print_list)-1
            else:# 아니면 대기열 -1
                target[_] -= 1
            # 앞에거 맨뒤로
            print_list.append(print_list[0])
            print_list.popleft()
        
