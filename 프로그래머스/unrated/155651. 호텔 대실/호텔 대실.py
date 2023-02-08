def solution(book_time):
    answer = 0
    room = []
    for t_in, t_out in book_time:
        room.append((convert_time(t_in), 1))
        room.append((convert_time(t_out)+10, 0))
    
    room.sort()
    tmp = 0
    for t, check in room:
        tmp += -1 if check == 0 else 1
        answer = max(answer, tmp)
    return answer
def convert_time(s):
    h, m = map(int, s.split(":"))
    return h*60 + m