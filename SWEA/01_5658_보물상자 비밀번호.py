# 1645 ~


# 회전가능
# 한면의 모든 숫자는 하나의 숫자의 각 자리수를 의미 함.(16진수)
# N을 queue에 담아서 로테이트 하며, 가능한 모든수 저장. 단 문자열 0x 뒤에 숫자 붙이고 hex함수

T= int(intput().rstrip())

for case in range(T):
    n,k = map(int,input().rstrip().split(" "))
