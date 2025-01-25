import sys


a,b = map(int,input().split())

if a==b:
    print("same")
else:
    print("A" if a>b else "B")