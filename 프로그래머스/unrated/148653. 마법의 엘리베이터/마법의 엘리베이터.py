def solution(storey):
    answer = 0
    while storey:
        r = storey % 10
        if r > 5 :
            answer += 10 - r
            storey += 10
        elif r == 5:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += r
        else:
            answer += r 
        storey //= 10
    return answer