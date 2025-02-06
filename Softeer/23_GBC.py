# 최대 100개 구간이므로 100개 배열구간의 규정, 실제 속도 저장
# 각 구간 실제 속도 - 규정 속도 의 최댓값 구하고, 0과 비교.
N,M = map(int,input().split())

v_limit = []
actual_vel = []

last = 1
for _ in range(N):
    s,v = map(int,input().split())
    for __ in range(last,last+s):
        v_limit.append(v)
    last += s

last = 1
for _ in range(M):
    s,v = map(int,input().split())
    for __ in range(last,last+s):
        actual_vel.append(v)
    last += s

max_vel_over = max(actual_vel[x] - v_limit[x] for x in range(100))
max_vel_over = max(max_vel_over,0)
print(max_vel_over)