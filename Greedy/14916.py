# 거스름돈

n=int(input())
coin = [5,2]
a=0
b=0
cnt=0
if n>=coin[0]:
    for _ in coin:
        cnt += n // _
        n %= _
    if n==0:print(cnt)
    else:
        while True:
            n+=coin[0]
            cnt -=1
            if n%coin[1]==0: 
                print(cnt + n//coin[1])
                break

else:
    cnt = n // coin[1]
    n %= coin[1]
    print(cnt if n==0 else -1)