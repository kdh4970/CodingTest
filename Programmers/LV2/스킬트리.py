# 2254 ~ 2410
def solution(skill, skill_trees):
    answer = 0
    d={}

    skill = list(skill)
    # print(skill)
    for test in skill_trees:
        
        test = list(test)
        level = -1
        # print(test)
        for _ in range(len(test)):
            if test[_] not in skill:
                test[_]=""
                continue
            if skill.index(test[_]) - level == 1:
                level +=1
                test[_]=""
                continue
            if skill.index(test[_]) - level >1:
                break
        
        # print(f"result : {test}")
        answer +=1 if "".join(test)=="" else 0
    return answer