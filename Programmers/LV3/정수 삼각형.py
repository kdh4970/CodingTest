# 1049 ~ 1136
# 위에서 내려가며 숫자의 합이 가장 큰 경우 찾기.
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 누적합을 기록하는 새 배열
# 7
# 10 15 
# 11 16 15
# 13 23 20 19 
# 단, 중복되는 칸에는 최댓값을 쓴다.

# i 2
# j 0~2
# j>=1


def solution(triangle):
    answer = 0
    height = len(triangle)
    sum_triangle = [[0]*x for x in range(1,height+1)]
    for i in range(height):# 0~ h-1
        if i == 0: 
            sum_triangle[0][0]=triangle[0][0]
            continue
        for j in range(i+1): # 0 ~ i-1
            if j==0:
                sum_triangle[i][j] = sum_triangle[i-1][j]+triangle[i][j]
            elif j==i:
                sum_triangle[i][j] = sum_triangle[i-1][j-1]+triangle[i][j]
            else:
                sum_triangle[i][j] = max(sum_triangle[i-1][j], sum_triangle[i-1][j-1])+triangle[i][j]
    answer = max(sum_triangle[height-1])
    return answer