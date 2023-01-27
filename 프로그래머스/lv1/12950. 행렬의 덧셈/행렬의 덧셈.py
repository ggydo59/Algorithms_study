def solution(arr1, arr2):
    answer = []
    
    for i, j in zip(arr1,arr2):
        answer.append([i[index]+j[index] for index in range(len(i))])
    return answer