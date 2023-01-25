import math
def get_fees(minutes, fees):
    return fees[1] + math.ceil(max(0,(minutes - fees[0])) / fees[2]) * fees[3]
def solution(fees, records):
    park_info = {}
    total_park_time = { key.split()[1]:0 for key in records }
    

    # 입차 출차 기록
    for record in records:
        time, num, inout = map(str, record.split())
        hour, minute = map(str, time.split(':'))
        time = int(hour) * 60 + int(minute)

        if inout == "IN":
            park_info[num] = [time,0]
        elif inout == "OUT":
            park_info[num][1] = time
            total_park_time[num] += park_info[num][1] - park_info[num][0]
            del park_info[num]

    # 총 주차기록 정산
    for key in park_info.keys():
        if park_info[key][1] == 0 :
            park_info[key][1] = 23 * 60 + 59
            total_park_time[key] += park_info[key][1] - park_info[key][0]

    del park_info     
    return [ get_fees(total_park_time[key],fees) for key in sorted(total_park_time.keys())]