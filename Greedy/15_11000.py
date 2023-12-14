# 강의실 배정

N = int(input())
time = []
ok = []
for _ in range(N):
    s,j = map(int,input().split())
    time.append((s,j))

room_cnt = 1

time.sort(key=lambda x : (x[1],x[0]))
temp_time=time
while True:
    before_end = temp_time[0][1]
    cnt = 1

    for _ in range(1,N):
        if temp_time[_][0] >= before_end:
            before_end = temp_time[_][1]
            cnt += 1
            del temp_time[_]

