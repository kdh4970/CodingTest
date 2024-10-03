### Attempt 1 : 24.10.03
### Time : 2016 ~  (m)

### solution
# numbers 갯수만큼 루프
# 147 L / 369 R / 2580 가까운 손 & 주손
lst_num=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

def get_distance(num1,num2):
    for r in range(len(lst_num)):
        for c in range(len(lst_num[0])):
            if lst_num[r][c]==num1:
                num1_r,num1_c=r,c
            if lst_num[r][c]==num2:
                num2_r,num2_c=r,c
    return abs(num1_r-num2_r)+abs(num1_c-num2_c)

def solution(numbers, hand):
    answer = ''
    last_r,last_l="*","#"
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            last_l = number
        elif number in [3,6,9]:
            answer += 'R'
            last_r = number
        else:
            dist_l = get_distance(number,last_l)
            dist_r = get_distance(number,last_r)
            if dist_l > dist_r: 
                answer += 'R'
                last_r = number
            elif dist_r > dist_l: 
                answer += 'L'
                last_l = number
            else: 
                if hand=="right":
                    answer += 'R'
                    last_r = number
                else:
                    answer += 'L'
                    last_l = number
            
    return answer