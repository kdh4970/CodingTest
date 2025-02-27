# 1501 ~ 1506

def solution(wallet, bill):
    answer = 0
    width,height = max(wallet),min(wallet)
    
    while min(bill) > height or max(bill) > width:
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        answer += 1
        
    return answer