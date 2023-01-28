def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    
    day = sum([i for i in days[:a-1]]) + (b - 1)    
    
    return answer[day%7]
