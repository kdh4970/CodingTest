# 1613 ~ 1645
# 재귀
# 영역 내 모든 수 동일 확인
# 동일 -> 통합
# 다름 -> 세분화
# Z 모양으로 순회
# 통합은 0->2, 1->-1로

new_arr = []
zeros,ones = 0,0
def solution(arr):
    global new_arr
    new_arr = arr
    
    def check(scope, start):
        r_range = (start[0], start[0]+scope)
        c_range = (start[1], start[1]+scope)
        temp = None
        for r in range(*r_range):
            for c in range(*c_range):
                if temp == None or temp ==arr[r][c] :temp=arr[r][c]; continue
                return False
        return True
    
    def write(scope, start):
        r_range = (start[0], start[0]+scope)
        c_range = (start[1], start[1]+scope)
        value = 2 if new_arr[start[0]][start[1]]==0 else -1
        for r in range(*r_range):
            for c in range(*c_range):
                new_arr[r][c] = value
    
    def func(scope, start):
        global new_arr,zeros,ones
        if check(scope,start):
            if new_arr[start[0]][start[1]]==0:
                zeros+=1
            else:
                ones+=1
            return
        scope //=2
        func(scope,start)
        func(scope,(start[0],start[1]+scope))
        func(scope,(start[0]+scope,start[1]))
        func(scope,(start[0]+scope,start[1]+scope))
        
        
    func(len(arr),(0,0))
    
    return [zeros,ones]