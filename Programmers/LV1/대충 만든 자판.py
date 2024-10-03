### Attempt 1 : 24.10.02
### Time : 2348 ~ 0023 (35m)

def make(target,keymap):
    lst=[0]*len(keymap)
    for idx,val in enumerate(keymap):
        for _ in range(len(val)):
            if val[_] == target:
                lst[idx] += _+1
                break
    return lst

def solution(keymap, targets):
    answer = [0]*len(targets)
    for idx,target in enumerate(targets):
        for char in target:
            out = make(char,keymap)
            if list(set(out)) == [0]:
                answer[idx] = -1
                break
            else:
                answer[idx] += min(x for x in out if x!=0)
    
    
    
    return answer