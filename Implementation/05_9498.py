# 시험 성적

SCORE = int(input())

rank = ""

if SCORE >= 90: rank="A"
elif SCORE >= 80: rank="B"
elif SCORE >= 70: rank="C"
elif SCORE >= 60: rank="D"
else: rank="F"

print(rank)