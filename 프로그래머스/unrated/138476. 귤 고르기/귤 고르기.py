def solution(k, tangerine):
    answer = 0
    dic = {key:0 for key in tangerine}
    
    for i in tangerine:
        dic[i] += 1
    s = sorted(dic.values())    
    v = 0
    while v < k :
        v += s.pop()
        answer += 1
    
    
    return answer

