# 1632 ~ 1659
def solution(msg):
    answer = []
    d={}
    offset = ord("A")
    for _ in range(26):
        d[chr(offset+_)] = _ + 1
    
    while msg:
        w,c ="",""
        for _ in range(len(msg)):
            if msg[:_+1] not in d:
                break
            w=msg[:_+1]
            c=msg[_+1] if _+1 < len(msg) else ""
        # print(w,c,d[w])
        answer.append(d[w])
        d[w+c] = len(d)+1
        msg = msg[len(w):]
    return answer