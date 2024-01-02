# 윤년

YEAR = int(input())

print(1 if (YEAR%4 == 0 and YEAR%100 != 0) or YEAR%400 == 0 else 0)