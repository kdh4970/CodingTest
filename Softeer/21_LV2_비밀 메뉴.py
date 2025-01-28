import sys

def input():
    return sys.stdin.readline().rstrip()

M,N,K = map(int,input().split())

secret_code = input()
user_input = input()

secret_code.replace(" ","")
user_input.replace(" ","")

print("normal" if user_input.find(secret_code)==-1 else "secret")