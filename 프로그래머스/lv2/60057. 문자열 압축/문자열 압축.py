def solution(s):
    """
    문자열내의 패턴을 찾는 문제
    1. 이중 포문 사용가능 s의 길이 1,000이하 예상 시간복잡도 O(N^2) 최악의 경우에 백만개 이므로
    2. Stack, deque 활용?
    """
    l = len(s)  
    answer = l
    for i in range(1, l//2+1):
        tmp = ""
        cnt = 0
        pre_str = s[:i]
        for j in range(0, l, i):
            target = s[j:j+i]
            if target == pre_str:
                cnt += 1
            else:          
                tmp += str(cnt) + pre_str if cnt > 1 else pre_str
                cnt = 1
                pre_str = target
                
        tmp += str(cnt) + pre_str if cnt > 1 else pre_str
        answer = min(answer, len(tmp))
    return answer