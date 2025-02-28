# 2128 ~ 2217
# 한자리 일때, 가능한 가짓수는 5
# A E I O U
# 두자리 일때, 5*(5+1) = 30
# A A(A~U) / E E(A~U)
# 세자리, 5*5*(5+1) = 150
# Axx AAx AA(A~U) / A AE AE(A~U)
d={"A":1, "E":2, "I":3, "O":4, "U":5, "x":0}

def solution(word):
    answer = 1
    while len(word)<5:
        word+="x"
    answer += 781*(d[word[0]]-1) # 첫글자
    if word[1] != "x": 
        answer += 156*(d[word[1]]-1)+1
        if word[2] != "x": 
            answer += 31 *(d[word[2]]-1)+1
            if word[3] != "x":
                answer += 6 * (d[word[3]]-1)+1
                if word[4] != "x":answer += d[word[4]]
    
    return answer