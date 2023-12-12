# 스택

def push(stack,x):
    stack.append(int(x))

def pop(stack):
    if len(stack) != 0: print(stack.pop())
    else: print("-1")

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack)==0: print("1")
    else: print("0")

def top(stack):
    if len(stack) != 0: print(stack[-1]) 
    else:print("-1")

def process_cmd(cmd_list,stack):
    for i in range(len(cmd_list)):
        cmd = cmd_list[i].split(" ")
        if cmd[0] == "size": size(stack)
        elif cmd[0] == "top": top(stack)
        elif cmd[0] == "empty": empty(stack)
        elif cmd[0] == "pop": pop(stack)
        elif cmd[0] == "push": push(stack,int(cmd[1]))

cmd_count=input()
cmd_list = []
stack=[]
for i in range(int(cmd_count)):
    cmd_list.append(input())

process_cmd(cmd_list,stack)
