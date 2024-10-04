### Attempt 1 : 24.10.04
### Time : 1716 ~ 1730 (14m)

def func(removed_zero,input_s):
    output_s = ""
    for _ in input_s:
        if _=="0":
            removed_zero += 1
        else:
            output_s += _
    output_s = bin(len(output_s))[2:]
    return removed_zero, output_s

def solution(s):
    
    num_removed_zero = 0
    cnt = 0
    while s!="1":
        cnt+=1
        num_removed_zero, s = func(num_removed_zero,s)
    
    
    return [cnt, num_removed_zero]