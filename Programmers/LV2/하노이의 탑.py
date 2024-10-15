answer=[]

def move(start,end):
    answer.append([start,end])
    
def hanoi(n,start,mid,end):
    if n==0:
        return
    hanoi(n-1,start,end,mid)
    move(start,end)
    hanoi(n-1,mid,start,end)

def solution(n):
    hanoi(n,1,2,3)
    return answer