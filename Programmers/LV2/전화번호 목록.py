# 1551 ~ 1647
# 
# 1차 솔루션 호율성 테스트 시간초과
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     n = len(phone_book)
#     for query_idx,query in enumerate(phone_book):
#         for data_idx in range(query_idx+1,n):
#             if query[0]!=phone_book[data_idx][0]:break
#             if phone_book[data_idx].startswith(query): return False
#     print(phone_book)
#     return answer

# 2차 솔루션
# 테케 하나 실패
# def solution(phone_book):
#     min_len = min([len(x) for x in phone_book])
#     n = len(phone_book)
#     new = set(list(map(lambda x : x[:min_len], phone_book)))
#     print(new)
#     if len(new) == n:return True
#     else: return False

# 3차 솔루션
def solution(phone_book):
    answer = True
    db = set(phone_book)
    for query in db:
        for i in range(len(query)):
            if query[:i] in db:
                return False
    
    return answer