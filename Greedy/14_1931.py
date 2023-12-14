# 회의실 배정

N = int(input())
time_info = []
for _ in range(N):
    start,end = map(int,input().split())
    time_info.append((start,end))
# 종료시간이 빠른 순으로 정렬 후 그 중 시작시간이 빠른 순 정렬
# 다음 회의 시작시간이 이전 회의 종료 시간보다 크거나 같을때, 조건에 부합하는 첫번째
time_info.sort(key = lambda x : (x[1], x[0]))
before_end = time_info[0][1]
cnt = 1
for _ in range(1,N):
    if time_info[_][0] >= before_end:
        before_end = time_info[_][1]
        cnt += 1


print(cnt)
