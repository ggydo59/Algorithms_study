from collections import Counter
def solution(participant, completion):        
    start = Counter(participant)
    end = Counter(completion)
    for i in start:
        if start[i] != end[i]:
            answer = i
    return answer
    
        