### Attempt 1 : 24.10.03
### Time : 1815 ~ 1707 (52m)

### solution
# 루프 순회 스코어 계산
# RT / CF / JM / AN

    
def solution(survey, choices):
    answer = ""
    scores = [0]*8 # R T C F J M A N
    d={}
    d["R"]=0
    d["T"]=1
    d["C"]=2
    d["F"]=3
    d["J"]=4
    d["M"]=5
    d["A"]=6
    d["N"]=7
    
    
    def add_score(survey_type,choice):
        # survey_type = "RT"
        # l_survey_type = "R"
        # r_survey_type = "T"
        l_survey_type = d[survey_type[0]]
        r_survey_type = d[survey_type[1]]
        
        if choice==1:scores[l_survey_type]+=3
        elif choice==2:scores[l_survey_type]+=2
        elif choice==3:scores[l_survey_type]+=1
        elif choice==4:pass
        elif choice==5:scores[r_survey_type]+=1
        elif choice==6:scores[r_survey_type]+=2
        elif choice==7:scores[r_survey_type]+=3
        
    for survey_type,choice in zip(survey,choices):
        add_score(survey_type,choice)
    print(scores)
    if scores[0]>scores[1]: answer = answer + "R"
    elif scores[0]<scores[1]: answer = answer + "T"
    else: answer = answer + "R"
    
    if scores[2]>scores[3]: answer = answer + "C"
    elif scores[2]<scores[3]: answer = answer + "F"
    else: answer = answer + "C"
    
    if scores[4]>scores[5]: answer = answer + "J"
    elif scores[4]<scores[5]: answer = answer + "M"
    else: answer = answer + "J"
    
    if scores[6]>scores[7]: answer = answer + "A"
    elif scores[6]<scores[7]: answer = answer + "N"
    else: answer = answer + "A"
        
            
    
    return answer