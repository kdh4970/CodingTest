from collections import Counter
import sys
def input(): return sys.stdin.readline().rstrip()

r,c,k = list(map(int,input().split(" ")))
arr=[[0]*100 for _ in range(100)]
for _ in range(3):
    elem= list(map(int,input().split(" ")))
    for __ in range(3):
        arr[_][__]=elem[__]

n,m=3,3
secs=0
# for ite in range(0,3):
while (arr[r-1][c-1]!=k):
    if secs==100:
        secs=-1
        break
    #1
    # 빈도 수 정렬을 위해, 해시사용
    if n>=m:
        for _ in range(n):
            temp=dict(Counter([arr[_][x] for x in range(m) if arr[_][x]]))
            unique_temp=sorted(temp.items(),key=lambda x:(x[1],x[0]))
            idx=0
            for val,freq in unique_temp:
                if val==0:continue
                arr[_][2*idx]=val
                arr[_][2*idx+1]=freq
                idx+=1
                if idx >= 50:
                    break
            idx*=2
            if m<idx:
                m=idx
            while idx < 50:
                arr[_][idx]=0
                idx+=1
        secs+=1
        continue
    #2
    else:
        for _ in range(m):
            temp=dict(Counter([arr[x][_] for x in range(n) if arr[x][_]]))
            unique_temp=sorted(temp.items(),key=lambda x:(x[1],x[0]))
            idx=0
            for val,freq in unique_temp:
                if val==0:continue
                arr[2*idx][_]=val
                arr[2*idx+1][_]=freq
                idx+=1
                if idx >= 50:
                    break
            idx*=2
            if n<idx:
                n=idx
            while idx < 50:
                arr[idx][_]=0
                idx+=1
        secs+=1
        continue
    
print(secs)