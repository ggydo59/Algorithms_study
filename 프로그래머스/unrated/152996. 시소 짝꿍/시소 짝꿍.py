from itertools import combinations

def solution(weights):
    answer = 0
    positions= [(2,3),(3,2),(2,4),(4,2),(3,4),(4,3)]
    w_dic = {i:0 for i in weights}

    
    for w in weights:
        w_dic[w] += 1
    
    for w in w_dic:
        # 같은 무게의 사람 중 2명을 뽑아서 count nC2
        if w_dic[w] > 1:
            answer += w_dic[w] * (w_dic[w] - 1) // 2
        
        # 포지션에 따른 토크를 계산하여 마주앉은 상대방의 몸무게를 계산
        # 해당 몸무게를 가진 인원 수 만큼 곱하여서 Count 해준다.
        for a, b in positions:
            others_w = w * a / b
            if others_w in w_dic.keys():
                answer += w_dic[w] * w_dic[others_w]
        w_dic[w] = 0
    return answer
        

    
    
    
        