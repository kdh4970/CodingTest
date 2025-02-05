import sys

s=input()

new_s = ""

new_s = s.replace("()","(1)")
new_s = new_s.replace(")(",")+(")

print(new_s)
