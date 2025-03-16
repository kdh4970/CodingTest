# 2100 ~ 2143
# 차량 번호가 작은 자동차부터, 청구할 주차요금 필요
# 차번 테이블 0000~9999 배열. 기본 -1
# 데이터 리스트는 누적 값, 입차 시간 저장
# record 읽으며, 새로운 차 들어오면 데이터 리스트 길이를 저장. 해당 차번 데이터가 데이터 리스트의 몇번째 위치하는지 매핑

def solution(fees, records):
    answer = []
    fromCarnumToIdx = [-1] * 10000
    datas = []
    for record in records:
        t,num,io = record.split(" ")
        num = int(num)
        if fromCarnumToIdx[num] == -1 and io == "IN":
            fromCarnumToIdx[num] = len(datas)
            hour, minute = map(int,t.split(":"))
            datas.append([0,minute + hour * 60])
        else:
            if io=="OUT" and datas[fromCarnumToIdx[num]][1] != -1:
                hour, minute = map(int,t.split(":"))
                datas[fromCarnumToIdx[num]][0] += (minute + hour * 60) - datas[fromCarnumToIdx[num]][1] 
                datas[fromCarnumToIdx[num]][1] = -1
            elif io=="IN" and datas[fromCarnumToIdx[num]][1] ==-1:
                hour, minute = map(int,t.split(":"))
                datas[fromCarnumToIdx[num]][1] = (minute + hour * 60)
                
    for _ in range(len(datas)):
        if datas[_][1]==-1:
            continue
        datas[_][0] += 59+23*60 - datas[_][1]
    for _ in fromCarnumToIdx:
        if _ == -1:
            continue
        totalTime = datas[_][0]
        if totalTime <= fees[0]:
            answer.append(fees[1])
        else:
            excess_time = totalTime - fees[0]
            q,l = excess_time//fees[2], excess_time % fees[2]
            excess_time = q + 1 if l !=0 else q
            additional = excess_time * fees[3]
            answer.append(fees[1] + additional)
            
    
    return answer