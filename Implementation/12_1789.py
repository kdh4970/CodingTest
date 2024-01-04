# 수들의 합
# N개의 자연수 합이 S일때, 자연수 N의 최댓값
# N개의 자연수가 1 간격일때, 즉, 이때의 합 S >= n*(n+1)/2
# n^2+n-2S<=0 의 양의 실근 x 보다 작은 값이 답.

from math import sqrt

S = int(input())

x= (-1+sqrt(1+8*S))//2
print(int(x))
