# 1043 ~ 1056
# 앞뒤 괄호 제거
# 배열에 {} 사이 값들 추가
# 정렬, a1=길이 하나 배열의 원소, a1을 다른 배열에 추가
# a2 = 다음 거에서 다른 배열에 없는 값 추가

def solution(s):
    s=s[1:-1]
    arr_lst = []
    start = 0
    for i in range(len(s)):
        if s[i] == "{":
            start = i
        elif s[i] =="}":
            arr_lst.append(list(map(int,s[start+1:i].split(","))))
            start = 0
        else:
            continue
    arr_lst.sort(key = lambda x:len(x))
    arr = []
    for array in arr_lst:
        for num in array:
            if num not in arr:
                arr.append(num)
    return arr
    
            
            