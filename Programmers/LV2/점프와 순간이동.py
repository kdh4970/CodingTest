# 1134 ~ 1200
# 현재까지 온 거리 x2로 순간이동 - 에너지 소모 0
# K칸 점프 - 에너지 소모 K
# 목적지 N까지 가는데 사용하는 에너지 소모의 최솟값.
# 현위치 *2가 N을 초과 하지 않는다면, 순간이동 또는 점프가능
# 현위치 *2가 N을 초과한다면, 점프만 가능.
# 
# N을 2로 계속해서 나누기.  5000 > 2500 > 1250 > 625> 624 > 312 > 156 > 78 > 39 > 38 > 19 > 18 > 9 > 8 > 4 > 2 >1 > 0
# 홀수라면 -1 
# 짝수면 나누기.
# N=0이 나올 때 까지



def solution(n):
    cost=0    
    while n>0:
        if n%2==1:
            n-=1
            cost += 1
        else:
            n /= 2

    return cost