# 생태학

import sys
def input():return sys.stdin.readline().rstrip()

db = dict()

total = 0
while True:
    tree = input()
    if tree == "":
        break
    else:
        if tree in db:
            db[tree] += 1
        else:
            db[tree] = 1
        total += 1

sdb = dict(sorted(db.items()))

for key,val in sdb.items():
    print(f"{key} {100 * val/total:.4f}")

