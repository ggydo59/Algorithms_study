from itertools import combinations as cb

def solution(numbers):
    return sorted(list(set([sum(i)for i in cb(numbers, 2)])))