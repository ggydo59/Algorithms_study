from itertools import product
def solution(users, emoticons):
    """
    1. 이모티콘 플러스 가입자 수 최대
    2. 이모티콘 매출액 최대
    
    모든 경우를 고려해도 할인률 종류는 4가지, 이모티콘의 종류는 7가지 이므로 2의 14승 =  16384 가지로 완전 탐색을 통해 구현할 수 있다.
    
    """
    answer = [0,0]
    for sales in product((10,20,30,40), repeat=len(emoticons)):
        sold = [0, 0] # [가입자수, 매출액]
        for u_sale, u_cash in users: # 유저기준 할인율, 유저기준 최소가입금액
            purchase = 0
            for emoticon, sale in zip(emoticons, sales): 
                if sale >= u_sale:
                    purchase += emoticon * (1 - (sale/100))
        
            if purchase >= u_cash:
                sold[0] += 1 # 구매금액이 u_cash보다 크거나 같을 경우 이모티콘 플러스 가입
            else:
                sold[1] += int(purchase) # 반대의 경우, 구매금액을 매출액에 더함
        answer = max(answer,sold) # 루프가 끝날때마다, 가입자수가 최대이고, 매출액이 최대인 경우로 answer 갱신

    return answer