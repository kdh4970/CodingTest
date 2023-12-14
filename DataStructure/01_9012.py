# 괄호

import sys
def input():
    return sys.stdin.readline().rstrip()

def chkVPS(text):
    if len(text) %2 ==1: print("NO");return
    for i in range(int(len(text)/2)):
        text = text.replace("()","");i+=1

    if len(text) == 0: print("YES"); return
    else: print("NO")

data_num = int(input())
data = []
for x in range(data_num):
    data.append(input())

for i in range(data_num): chkVPS(data[i])