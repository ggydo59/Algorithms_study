import heapq

def solution(n, k, enemy):
    heap = []
    l = len(enemy)
    if k >= l:
        return l
    
    for i in range(l):
        if n >= enemy[i]:
            n  -= enemy[i]
            heapq.heappush(heap, -enemy[i])
        else:
            if k > 0:
                if heap:
                    max_e = -heapq.heappop(heap)
                    k -= 1
                    if max_e > enemy[i]:
                        n += max_e - enemy[i]
                        heapq.heappush(heap, -enemy[i])
                    elif max_e == enemy[i]:
                        heapq.heappush(heap, -enemy[i])
                    else:
                        heapq.heappush(heap, -max_e)
                else:
                    k -= 1
            else:
                return i
        i += 1
        
    return l