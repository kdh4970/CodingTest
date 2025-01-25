import sys

N = int(input())
stations = [list(map(int,input().split())) for _ in range(N)]

min_station = [1000,1000]
for station in stations:
    if min_station[1] >= station[1]:
        min_station = station
print(min_station[0],min_station[1])