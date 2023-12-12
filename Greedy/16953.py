# A->B

a,b=list(map(int,input().split()))

cnt = 1
while True:
    if str(b)[-1]=="1":
        b=int(str(b)[:-1])
    elif str(b)[-1]=="2":
        b = int(b/2)
    elif int(str(b)[-1])%2 == 1:
        print(-1);break
    else:
        b = int(b/2)
    cnt += 1
    if b==a: print(cnt);break
    elif b<a: print(-1);break