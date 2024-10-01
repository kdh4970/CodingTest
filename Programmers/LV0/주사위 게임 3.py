### Attempt 1 : 24.10.02
### Time : 0040 ~ 0243 (123m)


def solution(a, b, c, d):
    answer = 0
    cnts={}
    for _ in [a,b,c,d]:
        if _ in cnts:
            cnts[_]+=1
        else:
            cnts[_]=1
    keys = list(cnts.keys()) ##  4 6 4 5
    values = list(cnts.values()) ## 2 1 2 1
    if 4 in values: answer=1111*keys[0]
    elif 3 in values:
        p=keys[values.index(3)]
        q=keys[values.index(1)]
        answer=(10*p+q)**2
    elif 2 in values:
        if values.count(2)==2:
            p,q=keys
            answer = (p+q)*abs(p-q)
        else: 
            p= keys[values.index(2)]
            q,r=[k for k in keys if k !=p ]
            
            answer = q*r
    else:
        answer=min(keys)
    return answer