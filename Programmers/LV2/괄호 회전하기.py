# 1703 ~ 1723
# 회전을 for문으로, 각각의 회전에서 온전한 문자열인지 체크
# 인덱싱은 0<=i<=n-1, i+1<=j<=i+n 까지, 단 인덱싱을 lst += s[j%n] 이런식으로
# () [] {}를 공백 대체를 반복하여 최종적으로 공백이면 온전한문자열
# 이러한 경우의 수를 카운트하여 리턴


def solution(s):
    answer = 0
    n=len(s)
    for i in range(n):
        ss = s[i]
        for j in range(i+1,i+n):
            ss += s[j%n]
        # print(ss)
        
        stk = []
        for c in ss:
            if not stk:
                stk.append(c)
            else:
                if (stk[-1]=="(" and c==")") or (stk[-1]=="[" and c=="]") or (stk[-1]=="{" and c=="}"):
                    stk.pop()
                    continue
                else:
                    stk.append(c)
        # print(stk)
        if not stk:
            answer += 1
        else:
            continue
    
    
    return answer