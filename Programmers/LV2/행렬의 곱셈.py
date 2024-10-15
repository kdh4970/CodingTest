# 2041 ~ 2054
# 
# r0c0 r0c1 ... r0cn  x  r0c0 ... r0cz  
# r1c0 r1c1 ... r1cn     r1c0
# ...
# rmc0 rnc1 ... rmcn     rnc0     rncz
# MxN * NxZ = MxZ
# 각 원소는 앞 배열의 행과 뒷 배열의 열 곱

def solution(arr1, arr2):
    M,N,Z = len(arr1),len(arr1[0]),len(arr2[0])

    answer = [[0]*Z for _ in range(M)]
    for r in range(M):
        for c in range(Z):
            for idx in range(N):          
                answer[r][c] += arr1[r][idx]*arr2[idx][c]
    
    return answer