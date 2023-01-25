def solution(k, tangerine):
    dic = {key:0 for key in tangerine}
    
    for i in tangerine:
        dic[i] += 1
    s = sorted(dic, key = lambda x:dic[x], reverse=True)
    v = 0
    for index, count in enumerate(s):        
        v += dic[count]
        if v >= k:
            s = s[:index+1]
            break
    
    
    return len(s)
