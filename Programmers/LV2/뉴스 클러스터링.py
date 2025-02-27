# 1726 ~ 1754

def solution(str1, str2):
    answer = 0
    a = [str1[x:x+2].lower() for x in range(len(str1)-1)]
    b = [str2[x:x+2].lower() for x in range(len(str2)-1)]
    
    a_ord = ord("a")
    z_ord = ord("z")

    new_a = []
    new_b = []
    for _ in a:
        if not (a_ord <= ord(_[0]) <= z_ord and a_ord <= ord(_[1]) <= z_ord):
            continue
        new_a.append(_)
    for _ in b:
        if not (a_ord <= ord(_[0]) <= z_ord and a_ord <= ord(_[1]) <= z_ord):
            continue
        new_b.append(_)
    # print(new_a)
    # print(new_b)
    
    if not new_a and not new_b: return 65536
    else:
        anb = 0
        aub = 0
        for _ in set(new_a):
            if _ in set(new_b):
                anb+=min(new_a.count(_), new_b.count(_))
                continue
        for _ in set(new_a+new_b):
            aub+=max(new_a.count(_), new_b.count(_))
                
        answer = anb / aub * 65536 
    return int(answer)