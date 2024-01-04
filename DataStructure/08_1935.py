# 후위 표기식2
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
Eq = input()

decoder = {}
symbol = ord("A")
for _ in range(N):
    decoder[chr(symbol+_)] = input()

decodedEq = []
for _ in Eq:
    decodedEq.append(decoder[_] if _ in decoder else _)

operator = ["/","*","+","-"]

def chkOperator(text:list, calculator : list) -> bool:
    for _ in text:
        if _ in calculator: return True
    return False

# find [num, num, operator] and calculate it
def doOnce(text:list)->list:
    for idx,val in enumerate(text):
        if val in operator:
            try:
                a=float(text[idx-2])
                b=float(text[idx-1])
                if val == "/": text[idx-2:idx+1] = [a/b]
                elif val == "*": text[idx-2:idx+1] = [a*b]
                elif val == "+": text[idx-2:idx+1] = [a+b]
                elif val == "-": text[idx-2:idx+1] = [a-b]
                return text
            except ValueError or IndexError:
                pass

while chkOperator(decodedEq,operator): # chechk if there is operator
    decodedEq = doOnce(decodedEq)
print("{0:0.2f}".format(decodedEq[0]))