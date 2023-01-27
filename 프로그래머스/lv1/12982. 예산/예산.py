def solution(d, budget):
    answer = 0
    money = 0
    d = sorted(d)
    
    for i in d:
        money += i
        if money > budget:
            break
        answer += 1
    return answer