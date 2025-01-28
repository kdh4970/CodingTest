import sys

def solution():
    land = [list(map(int,input().split())) for _ in range(3)]
    min_cost = 100
    # row check
    
    for line in land:
        if line[0]==line[1]==line[2]:
            min_cost=0
            return min_cost
        else:
            if line[0]==line[1]:
                temp = abs(line[1]-line[2])
                if temp<min_cost:
                    min_cost=temp
            elif line[0]==line[2]:
                temp = abs(line[0]-line[1])
                if temp<min_cost:
                    min_cost=temp
            elif line[1]==line[2]:
                temp = abs(line[1]-line[0])
                if temp<min_cost:
                    min_cost=temp
            else:
                if min_cost > 2:
                    min_cost=2
    for i in range(3):
        if land[0][i]==land[1][i]==land[2][i]:
            min_cost=0
            return min_cost
        else:
            if land[0][i]==land[1][i]:
                temp = abs(land[1][i]-land[2][i])
                if temp<min_cost:
                    min_cost=temp
            elif land[0][i]==land[2][i]:
                temp = abs(land[0][i]-land[1][i])
                if temp<min_cost:
                    min_cost=temp
            elif land[1][i]==land[2][i]:
                temp = abs(land[1][i]-land[0][i])
                if temp<min_cost:
                    min_cost=temp
            else:
                if min_cost > 2:
                    min_cost=2
    return min_cost

print(solution())