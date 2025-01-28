import sys

numT= int(input())
T = [list(input().split()) for _ in range(numT)]

####
#  0
# 1 2
#  3
# 4 5
#  6

table = [
    [True,True,True,False,True,True,True], #0
    [False,False,True,False,False,True,False], #1
    [True,False,True,True,True,False,True], #2 
    [True,False,True,True,False,True,True], #3
    [False,True,True,True,False,True,False], #4
    [True,True,False,True,False,True,True], #5
    [True,True,False,True,True,True,True], #6
    [True,True,True,False,False,True,False], #7
    [True,True,True,True,True,True,True], #8
    [True,True,True,True,False,True,True], #9
]

# 12345가 숫자로 들어오면 배열에 역순 저장
for test in T:
    res = 0
    before = [int(test[0][x]) for x in range(-1,-1-len(test[0]),-1)]
    after = [int(test[1][x]) for x in range(-1,-1-len(test[1]),-1)]
    lb = len(before)
    la = len(after)
    if lb == la :
        for _ in range(la):
            query_before = table[before[_]]
            query_after = table[after[_]]
            for i in range(7):
                if query_before[i] != query_after[i]:
                    res+=1
    elif lb > la:
        d = lb-la
        for x in range(-1,-1-d,-1):
            query_before = table[before[x]]
            res += sum(query_before)
        for _ in range(la):
            query_before = table[before[_]]
            query_after = table[after[_]]
            for i in range(7):
                if query_before[i] != query_after[i]:
                    res+=1
    elif lb < la:
        d = la-lb
        for x in range(-1,-1-d,-1):
            query_after = table[after[x]]
            res += sum(query_after)
        for _ in range(lb):
            query_before = table[before[_]]
            query_after = table[after[_]]
            for i in range(7):
                if query_before[i] != query_after[i]:
                    res+=1           
    print(res)