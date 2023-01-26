def solution(absolutes, signs):
    i = 0
    answer = 0
    
    while i < len(signs):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        i += 1
    return answer