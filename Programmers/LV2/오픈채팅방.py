# 1632 ~ 1641

def solution(record):
    answer = []
    d= {}
    for r in record:
        t= r.split(" ")
        if len(t) == 3:
            io,uid,name = t
            d[uid] = name
    for r in record:
        t = r.split(" ")
        if t[0]=="Enter":
            answer.append(f"{d[t[1]]}님이 들어왔습니다.")
            continue
        if t[0]=="Leave":
            answer.append(f"{d[t[1]]}님이 나갔습니다.")
            continue
    return answer