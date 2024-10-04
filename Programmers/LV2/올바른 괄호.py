### Attempt 2 : 24.10.04
### Time : 1313 ~ 1319 (6m)

# arr에 여는괄호 있고, 다음 입력이 닫는괄호면 arr pop 후 continue
# 마지막 arr 길이체크

def solution(s):
    # while True:
    #     if len(s)==0: return True
    #     if s.startswith(")")or s.endswith("("):
    #         return False
    #     t=s.replace("()","")
    #     if t==s: 
    #         if len(s) !=0: return False
    #     s=t
    arr = []
    if s[0]==")" or s[-1]=="(": return False
    for _ in s:
        if arr and arr[-1]=="(" and _==")" :
            arr.pop()
        else:
            arr.append(_)
    if arr: return False
    else: return True 