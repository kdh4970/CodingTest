# 1603 ~ 1630
# 
def isNum(x):
    return True if ord("0") <= ord(x) <= ord("9") else False


def solution(files):
    breaked = []
    for file in files:
        temp =[]
        pos = 0
        for _ in range(len(file)):
            if pos==0 and isNum(file[_]):
                temp.append(file[:_])
                pos = _
                if _==len(file)-1:
                    temp.append(file[_]);break
                continue
            if pos >0 and _==len(file)-1:
                temp.append(file[pos:])
                break
            if pos >0 and not isNum(file[_]):
                temp.append(file[pos:_])
                pos = -_
                continue
            if pos < 0 and _ == len(file)-1:
                temp.append(file[-pos:])
            
        breaked.append(temp)
    breaked.sort(key = lambda x:(x[0].lower(),int(x[1])))
    
    return ["".join(b) for b in breaked]