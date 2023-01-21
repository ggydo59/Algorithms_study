def solution(N, stages): 
    dic = {key:[0,0,0] for key in range(1,N+2)}
    temp = 0
    # [스테이지 머문인원, 스테이지 도달한 인원, 실패율]
    for key in stages:
        dic[key][0] += 1
        
    # 실패율 계산
    for key, value in dic.items():
        if key == N+1:break
    
        dic[key][1] = len(stages) - temp
        temp += value[0]
        if dic[key][0] == 0 : dic[key][2] = 0
        else:
            dic[key][2] = dic[key][0] / dic[key][1]
        
    # 실패율에 따른 내림차순 정렬
    dic.pop(N+1)
    dic = sorted(dic.items(), key=lambda x: x[1][2], reverse=True)
    
    
    return [dic[i][0] for i in range(N)]