import sys

N = int(input())

lst = []

for _ in range(N):
    n=input()
    if n.find(".")==-1:
        lst.append((int(n),-1))
    else:
        x,y = n.split(".")
        lst.append((int(x),int(y)))

lst.sort()

for i in lst:
    if i[1]==-1:
        print(i[0])
    else:
        print(f"{i[0]}.{i[1]}")
