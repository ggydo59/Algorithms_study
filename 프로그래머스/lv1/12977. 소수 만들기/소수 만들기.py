from itertools import combinations
def solution(nums):
    answer = 0
    
    numbers = [ sum(i) for i in combinations(nums,3)]
    
    for i in numbers:
        a = True
        for j in range(2,int(i**0.5)+1):         
                if i % j == 0:
                    a = False
        if a:
            answer += 1  
    return answer