# 1508 ~ 1533

def solution(s):
    answer = 0
    stop = False
    while not stop:
        x = s[0]
        cnt_x = 0
        cnt_nx = 0
        for i in range(len(s)):
            if s[i]==x:
                cnt_x+=1
            else:
                cnt_nx+=1
            if (cnt_x == cnt_nx) and i > 0:
                if i==len(s)-1: stop=True
                # print(s[:i+1], s[i+1:])
                s=s[i+1:]
                answer+=1
                break
            elif i==len(s)-1: stop=True;answer+=1
    
    return answer