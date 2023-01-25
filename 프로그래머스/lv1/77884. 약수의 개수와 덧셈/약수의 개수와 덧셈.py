def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        j = 1
        while j * j <= i:
            if(j*j == i):count +=1
            elif i % j == 0: count += 2
            j += 1
            
                  
        if count % 2 == 0:
            answer += i
        elif count % 2 == 1:
            answer -= i
    return answer