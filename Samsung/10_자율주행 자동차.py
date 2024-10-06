import sys
def input():
    return sys.stdin.readline().rstrip()

n,m = list(map(int,input().split(" ")))
x,y,d_idx = list(map(int,input().split(" ")))
# 0-도로 1-인도 2-방문
road = [list(map(int,input().split(" "))) for _ in range(n)] 

directions=[(-1,0),(0,1),(1,0),(0,-1)]
road[x][y] = 2
visited=1

def func():
    global d_idx,x,y,visited
    for _ in range(4):
        #1
        d_idx = d_idx-1 if d_idx>0 else 3
        if road[x+directions[d_idx][0]][y+directions[d_idx][1]]==0:

            # print(f"Move from {x},{y} to {x+directions[d_idx][0]},{y+directions[d_idx][1]}")
            x+=directions[d_idx][0]
            y+=directions[d_idx][1]
            road[x][y]=2
            visited+=1
            return 1 # next
        #2
        else:
            if _==3:
                if road[x-directions[d_idx][0]][y-directions[d_idx][1]]!=1:
                    x-=directions[d_idx][0]
                    y-=directions[d_idx][1]
                    return 1 # again
                else:
                    return 0 # stop
            else:
                continue
res=1
while res:
    res=func()
print(visited)
        