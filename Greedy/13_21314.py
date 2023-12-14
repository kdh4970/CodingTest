# 민겸 수

mk_str = input()

mk_max=[]
mk_min=[]
m=0
# K 가 나올떄 까지 M 카운트
for _ in range(len(mk_str)):
    if mk_str[_] == "M":
        m+=1
        if _ == len(mk_str)-1:
            mk_max.append(str(1)*m)
            mk_min.append(str(10**(m-1)))
    else:
        mk_max.append(str(5*(10**(m))))
        if m != 0:
            mk_min.append(str(10**(m-1)))
        mk_min.append(str(5))
        m=0
print("".join(mk_max))
print(int("".join(mk_min)))
