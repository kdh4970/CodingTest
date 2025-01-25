import sys
a,b,d = map(int,input().split())

t1=0
t2=0
dist = d
isfront = False
while dist > 0:
    if not isfront:
        if dist>a:
            t1+=a
            dist-=a
            isfront = not isfront   
            continue
        else:
            t1+=dist
            dist=0
            break
    else:
        t1+=b
        isfront= not isfront
        continue
dist=d
while dist > 0:
    if not isfront:
        if dist>b:
            t2+=b
            dist-=b
            isfront = not isfront   
            continue
        else:
            t2+=dist
            dist=0
            break
    else:
        t2+=a
        isfront= not isfront
        continue
print(t1+t2)