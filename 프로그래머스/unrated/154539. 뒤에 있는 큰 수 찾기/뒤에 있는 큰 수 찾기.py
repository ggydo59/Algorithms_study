def solution(numbers):
    answer = [-1] * len(numbers)
    s = []
    for idx in range(len(numbers)):
        while s and numbers[idx] > numbers[s[-1]]:
            answer[s.pop()] = numbers[idx]
        s.append(idx)

        
        
        
    return answer