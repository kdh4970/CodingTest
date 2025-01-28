import sys

# 간격    1 2 3 4 
# 점 갯수 4 9 16 25

# 1회 4->9 f(2)   f(2^1)
# 2회 9->25 f(4)  f(2^2)
# 3회 25-> f(8)   f(2^3)

N = int(input())


def f(x):
    return (x+1)**2

print(f(2**N))
