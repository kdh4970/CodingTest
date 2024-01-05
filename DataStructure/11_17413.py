# 단어 뒤집기 2
S = input()

stk = []
res = ""
isTag=False
idx = 0

for idx,val in enumerate(S):
    if val == "<":
        isTag=True
        if stk:
            for _ in range(len(stk)):
                res += stk[-1-_]
            stk=[]
    stk.append(val)
    

    if val == ">":
        res += "".join(stk)
        stk = []
        isTag=False
    
    elif val == " ":
        if isTag:
            pass
        else:
            stk.pop()
            for _ in range(len(stk)):
                res += stk[-1-_]
            res += " "
            stk=[]
    elif idx == len(S)-1:
        for _ in range(len(stk)):
            res += stk[-1-_]
    

print("".join(res))
