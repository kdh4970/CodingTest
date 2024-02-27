# 곱셈 
# 시간제한 0.5초
import sys
def input():return sys.stdin.readline().rstrip()

A,B,C = list(map(int,input().split()))

def func(a,b,c):
    if b==0:return

    if b%2 ==1:
        temp = 
        return 
    else:
        temp=func()
    func(a,b,c)

ans = func(A,B,C)
print(ans)