import sys

n = int(input())
f = list(map(int,input().split()))

max_val = -100000
for a in range(n):
    for b in range(a+1,n):
        mul = f[a]*f[b]
        if max_val < mul:
            max_val = mul
print(max_val)