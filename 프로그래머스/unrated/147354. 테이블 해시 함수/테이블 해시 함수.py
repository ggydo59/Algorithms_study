def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        answer ^= sum(list(map(lambda x : x % (i+1), data[i])))
                      
    return answer 