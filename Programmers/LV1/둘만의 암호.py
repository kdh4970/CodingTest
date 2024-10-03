### Attempt 1 : 24.10.03
### Time : 1505 ~ 1606 (61m)

# s의 각 원소에 대해 인덱스 만큼의 크기를 갖는 리스트 생성
# 리스트의 값에서 skip 중복시 제거하고 다음 문자 추가 ## 반복
def solution(s, skip, index):
    answer = ''
    n_skip = list(map(ord,skip))
    for c in s:
        new_c = ord(c)
        for _ in range(index):
            new_c=new_c+1 if new_c <ord("z") else ord("a")
            while True:
                if new_c in n_skip:
                    new_c=new_c+1 if new_c <ord("z") else ord("a")
                    continue
                break
        answer+=chr(new_c)
            
        
    return answer