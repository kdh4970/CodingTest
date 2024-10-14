## 1340 ~ 1353 (13m)

# words에서 아래 조건 체크
# 이어지지 않는 문자 or 중복 단어

# k개 중 idx가 탈락이라면
# 가장 먼저 탈락하는 사람의 번호와 차례를 반환
# 번호 = idx % n
# 차례 = idx // n + 1

def solution(n, words):
    visited = set()
    last_char=words[0][0]
    for idx,word in enumerate(words):
        if last_char != word[0]:
            return [(idx%n) + 1,(idx // n) + 1]
        else:
            if word not in visited:
                visited.add(word)
                last_char=word[-1]
                continue
            else:
                return [(idx%n) + 1,(idx // n) + 1]
    return [0,0]
        
        