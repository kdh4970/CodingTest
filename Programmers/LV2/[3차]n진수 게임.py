# 1530 ~ 1629
# 18 > 9 0 > 4 1 > 2 0 > 1 0
# 10010
d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def convert(n,to):
    if n == 0:
        return "0"
    
    divider = 1
    res = ""
    while n>0:
        nameoji = n%to
        if nameoji<10:
            res = str(nameoji) + res
        else:
            res = d[nameoji] + res
        n//=to
    return res

def solution(n, t, m, p):
    answer = ''
    num = 0
    seq = 1
    cnt_answer = 0
    while cnt_answer < t:
        target_num_str = convert(num,n)
        for _ in target_num_str:
            if (m!=p and seq%m == p) or (m==p and seq%m==0):
                answer += _
                cnt_answer += 1
            if cnt_answer == t:
                return answer
            seq +=1
        num+=1
    return answer