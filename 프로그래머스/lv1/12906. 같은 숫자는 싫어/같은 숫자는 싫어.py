def solution(arr):
    answer = [arr[0]]
    
    temp = arr[0]
    
    for i in arr:
        if i != temp:
            temp = i
            answer.append(i)
    
    return answer