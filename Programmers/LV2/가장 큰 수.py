# 2056 ~ 2225
# 0인 경우 예외처리 
def solution(numbers):
    s_numbers = list(map(str,numbers))
    s_numbers.sort(reverse=True,key = lambda x:(x*3)[:4])
    return "".join(s_numbers) if "".join(s_numbers)[0] !="0" else "0" 