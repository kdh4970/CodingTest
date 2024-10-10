# 회전가능
# 한면의 모든 숫자는 하나의 숫자의 각 자리수를 의미 함.(16진수)
# N을 queue에 담아서 로테이트 하며, 가능한 모든수 저장. 단 문자열 0x 뒤에 숫자 붙이고 hex함수



from collections import deque

T=int(input().rstrip( ))

vals=set()
def rotate(q, start, end):
    if start == end:
        return
    for _ in range(4):
        str_num=list(q)[end*_:end*(_+1)]
        str_num = "".join(str_num)
        # print(str_num)
        str_num = int(str_num,16)
        if str_num not in vals:
            vals.add(str_num)

    q.rotate(1)
    rotate(q,start+1,end)




for case in range(T):
    n,k = map(int,input().rstrip().split(" "))
    str_numbers=input()
    q=deque([x for x in str_numbers])
    vals=set()
    rotate(q,0, n//4)
    # print(vals)
    # print("\n result \n")
    vals=list(vals)
    vals=sorted(vals,reverse=True)
    # print(vals)
    print(f"#{case+1} {vals[k - 1]}")
