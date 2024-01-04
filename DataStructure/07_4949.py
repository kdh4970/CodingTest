# 균형잡힌 세상


while True:
    text = input()
    if text == ".": break
    stack = []
    for _ in text:
        if _ in "([":
            stack.append(_)
        elif _==")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append("fail")
                break
        elif _== "]":
            if stack and stack[-1] =="[":
                stack.pop()
            else:
                stack.append("fail")
                break
        else:
            pass
    print("no" if stack else "yes")