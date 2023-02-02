def solution(k,ranges):
    answer  = []
    area, axis = [],[]
    while k != 1:
        axis.append(k)            
        if k % 2 == 0:
            k = k // 2            
        else:
            k = (k * 3) + 1                    
    axis.append(k)    
    for i in range(1, len(axis)):
        temp = (abs(axis[i] - axis[i-1]) / 2) + min(axis[i], axis[i-1])
        area.append(temp)
    for i,j in ranges:
        temp = sum(area[i:len(area)+j])
        if i > len(area) + j:        
            answer.append(-1)
        else:
            answer.append(temp)


    return answer