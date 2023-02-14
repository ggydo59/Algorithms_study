from itertools import product as p
import math

def solution(k, d):
    """
    product을 이용한 풀이 -> 시간초과
    """
    # dot = [ i for i in range(0, d+1, k)]
    # answer = [ (i,j) for i, j in p(dot, repeat=2)  if ((i**2) + (j**2)) ** 0.5 <= d]
    
    """
    x좌표를 먼저 구하고, x좌표에 따른 y좌표의 최대값을 구한뒤 k로 나누고 x축 위의 점을 고려하여 1을 더한다.
    """
    #answer = 0
    #for x in range(0, d+1, k):
    #   y = math.sqrt(d**2 - x**2)      
    #    answer += math.floor(y/k) + 1
    #    print(y,answer)
    """
    리스트 컴프리헨션 활용 one_line 풀이
    """
    return sum([math.floor(math.sqrt(d**2 - x**2)/k)+1 for x in range(0, d+1,k)])
    
    