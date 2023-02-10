from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    
    t = [0] * (y+1)
    
    t[x] = 1
    q = deque()
    q.append(x)
    
    while q:
        x = q.popleft()
        
        if x*3 <= y and t[x*3] == 0:
            t[x*3] = t[x] + 1
            q.append(x*3)

        if x*2 <= y and t[x*2] == 0:
            t[x*2] = t[x] + 1
            q.append(x*2)

        if x+n <= y and t[x+n] == 0:
            t[x+n] = t[x] + 1        
            q.append(x+n)
        if x > y:
            break
        if x== y:
            return t[x] - 1
    

        
    return -1
    
    
        
    
        
        
        
   