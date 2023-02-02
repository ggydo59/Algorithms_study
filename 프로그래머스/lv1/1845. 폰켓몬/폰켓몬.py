def solution(nums):
    monster = len(nums) // 2
    a = len(set(nums))
    
    if monster > a:
        return a
    else:
        return monster
    
