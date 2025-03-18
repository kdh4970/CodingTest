# 2009 ~ 2053
# 1인 비트 냅두고 가장 앞에있는 0인비트를 1로?
# 111이면 가장 앞에걸 쉬프트해서 1011
# 사이에 01을 10으로
# 0을1로
def f(x):
    bit_x=[i for i in str(bin(x))[2:]]
    if x == 0: return 1
    if sum(map(int,bit_x))==len(bit_x):
        bit_x[0] = "0"
        y="0b1" + "".join(bit_x)
    else:
        l=len(bit_x)-1
        for _ in range(l):
            if bit_x[l-_-1] == "0" and bit_x[l-_]=="1":
                bit_x[l-_-1] ="1"
                bit_x[l-_] = "0"
                break
            elif bit_x[l-_] == "0":
                bit_x[l-_] ="1"
                break
            else:
                continue
        y="0b" + "".join(bit_x)
    # print(f"{x}:{str(bin(x))[2:]} converted to {int(y,2)}:{y}")
    return int(y,2)
    
def solution(numbers):
    answer = []
    # for _ in range(100):
    #     answer.append(f(_))
    for number in numbers:
        answer.append(f(number))
    return answer