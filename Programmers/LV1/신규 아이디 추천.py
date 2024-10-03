### Attempt 1 : 24.10.03
### Time : 2037 ~ 2122 (45m)

def solution(new_id):
    answer = ''
    #1
    new_id=new_id.lower()
    #2
    for c in new_id:
        if ord("a")<=ord(c)<=ord("z") or (c in list(map(str,range(0,10)))) or c in ["-","_","."]: 
            answer += c
    #3
    lst_dot =[]
    length=0
    for _ in range(len(answer)):
        if _>0 and answer[_-1]==answer[_]==".":
            length += 1
            if _ == len(answer)-1:
                lst_dot.append(length)
        else:
            if length !=0: 
                lst_dot.append(length)
                length = 0
    for _ in lst_dot:
        answer = answer.replace("."*(_+1),".",1)
    #4
    if len(answer)>0:
        if answer[0]==".":
            answer=answer.replace(".","",1)
        if len(answer) > 1 and answer[len(answer)-1]==".":
            answer=answer[:len(answer)-1]
    #5
    if len(answer) == 0:
        answer += "a"
    #6
    if len(answer)>=16:
        answer=answer[:15]
        if answer[14]==".":
            answer=answer[:14]
    #7
    while len(answer)<=2:
        answer+=answer[len(answer)-1]
    return answer