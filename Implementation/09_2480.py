# 주사위 세개

A,B,C = list(map(int,input().split()))

reward = 0

if A==B and B==C: reward = 10000+A*1000
elif A==B: reward = 1000+A*100
elif B==C: reward = 1000+B*100
elif A==C: reward = 1000+C*100
else:reward = max((A,B,C))*100

print(reward)