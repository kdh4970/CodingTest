# 숨바꼭질3 
# 시간제한 2초
# 순간이동 - 시간소모 0초 현위치의 2배수
# 걷기 - 시간소모 1초, 현위치 +-1

# 일반적인 bfs는 x,y에 대해 x,y의 값을 다룸.
# 본 문제는 x,y에 대해 n*2^x+y = K

from collections import deque
import sys
def input():return sys.stdin.readline().rstrip()

N,K = list(map(int,input().split()))
MAX = 100001
q = deque()
q.append(N)
visited = [-1]*MAX
visited[N]=0

while q:
    now = q.popleft()
    if now == K:
        print(visited[now])
        break

    if 0 <= now*2 < MAX and visited[now*2] == -1:
        q.appendleft(now*2)
        visited[now*2] = visited[now]
    if 0 <= now-1 < MAX and visited[now-1] == -1:
        q.append(now-1)
        visited[now-1] = visited[now]+1
    if 0 <= now+1 < MAX and visited[now+1] == -1:
        q.append(now+1)
        visited[now+1] = visited[now]+1
